#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2018 Alexander Maul
#
# Ported to Py3  09/2018
#
# Author(s):
#
#   Alexander Maul <alexander.maul@dwd.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
trollbufr-Subset
================
The class doing all decoding, table-loading, etc in the right order.

Created on Oct 28, 2016

@author: amaul
"""
from . import functions as fun
from . import operator as op
from .errors import BufrDecodeError, BufrEncodeError
from .bufr_types import DescrDataEntry, AlterState, BackrefRecord
import logging

logger = logging.getLogger("trollbufr")


class SubsetReader(object):
    # Numbering of this subset (this, total)
    subs_num = (-1, -1)
    # Compression
    is_compressed = False
    # Currently decoding a subset
    inprogress = False

    def __init__(self, tables, bufr, descr_list, is_compressed, subset_num,
                 data_end, edition=4, has_backref=False, as_array=False):
        # Apply internal compression
        self.is_compressed = is_compressed
        # BUFR edition
        self.edition = edition
        # Current and total number of subsets, as tuple
        self.subs_num = subset_num
        # Holds table object
        self._tables = tables
        # Holds byte array with bufr
        self._blob = bufr
        # Initial descriptor list
        self._desc = descr_list
        # End of data for all subsets
        self._data_e = -1
        # Alterator values
        self._alter = AlterState()
        # Skip N data descriptors
        self._skip_data = 0
        # Recording descriptors for back-referencing
        self._do_backref_record = has_backref
        # Recorder for back-referenced descriptors
        self._backref_record = BackrefRecord()
        # Last octet in BUFR
        self._data_e = data_end
        # Variable names for positioning/current working list in descriptor/value lists:
        # dl : current descriptor list
        # di : index for current descriptor list
        # de : stop when reaching this index
        # vl : values list; compression: list of all subsets, otherwise: one subset's data
        # vi : value list index
        self._dl = []
        self._di = self._de = 0
        self._vl = []
        self._vi = 0
        self._as_array = as_array and self.is_compressed
        # Method for reading a value from the bistream, depends on compression.
        if self._as_array and self.is_compressed:
            self.get_val = fun.get_val_array
        elif self.is_compressed:
            self.get_val = fun.get_val_comp
        else:
            self.get_val = fun.get_val

    def __str__(self):
        return "Subset #%d/%d, decoding: %s" % (self.subs_num[0],
                                                self.subs_num[1],
                                                self.inprogress)

    def next_data(self):
        """Iterator for Sect. 4 data.

        This generator will decode BUFR data.

        For each data element a named tuple is returned.
        The items are the descriptor, a type marker, a numerical value, and
        quality information. Items unset or unapplicaple are set to None.

        If the reader is set to return all subsets' values as an array per
        descriptor, the yielded value and quality data are both a list of equal
        size. Otherwise both are simple data types.

        mark consists of three uppercase letters, a space character, and a
        descriptor or iteration number or "END".
        When a value for mark is returned, the others items are usually None,
        mark has the meaning:
        - SEQ desc : Following descriptors by expansion of sequence descriptor desc.
        - SEQ END  : End of sequence expansion.
        - RPL #n   : Descriptor replication number #n begins.
        - RPL END  : End of descriptor replication.
        - RPL NIL  : Descriptor replication evaluated to zero replications.
        - REP #n   : Descriptor and data repetition, all descriptor and data
                     between this and REP END are to be repeated #n times.
        - REP END  : End of desriptor and data repetition.
        - OPR desc : Operator, which read and returned data values.
        - BMP      : Use the data present bit-map to refer to the data descriptors
                     which immediately precede the operator to which it relates.
                     The bitmap is returned in the named tuple item 'value'.

        :yield: collections.namedtuple(desc, mark, value, quality)
                OR collections.namedtuple(desc, mark, [value, ...], [quality, ...])
        """
        if self._blob.p < 0 or self._data_e < 0 or self._blob.p >= self._data_e:
            raise BufrDecodeError("Data section start/end not initialised!")
        logger.debug("SUBSET START")
        self.inprogress = True
        # Stack for sequence expansion and loops.
        # Items follow: ([desc,], start, end, mark)
        stack = []
        # Alterator values, this resets them at the beginning of the iterator.
        self._alter.reset()
        # For start put list on stack
        logger.debug("PUSH start -> *%d %d..%d", len(self._desc), 0, len(self._desc))
        stack.append((self._desc, 0, len(self._desc), "SUB"))
        while len(stack):
            """Loop while descriptor lists on stack"""
            # dl : current descriptor list
            # di : index for current descriptor list
            # de : stop when reaching this index
            self._dl, self._di, self._de, mark = stack.pop()
            logger.debug("POP *%d %d..%d (%s)", len(self._dl), self._di, self._de, mark)
            yield DescrDataEntry(None, mark, None, None)
            mark = None
            while self._di < self._de and self._blob.p < self._data_e:
                """Loop over descriptors in current list"""

                if self._skip_data:
                    """Data not present: data is limited to class 01-09,31"""
                    logger.debug("skip %d", self._skip_data)
                    self._skip_data -= 1
                    if 1000 <= self._dl[self._di] < 10000 and self._dl[self._di] // 1000 != 31:
                        self._di += 1
                        continue

                if fun.descr_is_nil(self._dl[self._di]):
                    """Null-descriptor to signal end-of-list"""
                    self._di += 1

                elif fun.descr_is_data(self._dl[self._di]):
                    """Element descriptor, decoding bits to value"""
                    # Associated fields (for qualifier) preceede the elements value,
                    # their width is set by an operator descr.
                    # They are handled in compression in same manner as other descr,
                    # with fix width from assoc-field-stack.
                    if self._alter.assoc[-1] and (self._dl[self._di] < 31000 or self._dl[self._di] > 32000):
                        qual = self.get_val(self._blob,
                                            self.subs_num,
                                            fix_width=self._alter.assoc[-1])
                    else:
                        qual = None
                    try:
                        elem_b = self._tables.tab_b[self._dl[self._di]]
                    except KeyError as e:
                        raise BufrDecodeError("Unknown descriptor {}".format(e))
                    self._di += 1
                    value = self.get_val(self._blob,
                                         self.subs_num,
                                         elem_b,
                                         self._alter)
                    if self._do_backref_record:
                        self._backref_record.append(elem_b, self._alter)
                    # This is the main yield
                    yield DescrDataEntry(elem_b.descr, mark, value, qual)

                elif fun.descr_is_loop(self._dl[self._di]):
                    """Replication descriptor, loop/iterator, replication or repetition"""
                    loop_cause = self._dl[self._di]
                    # Decode loop-descr:
                    loop_amount, loop_count, is_repetition = self.eval_loop_descr()
                    # Current list on stack (di points after looped descr)
                    logger.debug("PUSH jump -> *%d %d..%d", len(self._dl), self._di + loop_amount, self._de)
                    if is_repetition:
                        if loop_count:
                            stack.append((self._dl, self._di + loop_amount, self._de, "REP END"))
                            stack.append((self._dl, self._di, self._di + loop_amount, "REP %d" % loop_count))
                        else:
                            stack.append((self._dl, self._di + loop_amount, self._de, "REP NIL"))
                    else:
                        ln = loop_count
                        stack.append((self._dl, self._di + loop_amount, self._de, "RPL %s" % ("END" if ln else "NIL")))
                        while ln:
                            # N*list on stack
                            logger.debug("PUSH loop -> *%d %d..%d", len(self._dl), self._di, self._di + loop_amount)
                            stack.append((self._dl, self._di, self._di + loop_amount, "RPL %d" % ln))
                            ln -= 1
                    yield DescrDataEntry(None,
                                         "%s %06d *%d" % (
                                             "REP" if is_repetition else "RPL",
                                             loop_cause,
                                             loop_count),
                                         None,
                                         None)
                    # Causes inner while to end
                    self._di = self._de

                elif fun.descr_is_oper(self._dl[self._di]):
                    """Operator descritor, alter/modify properties"""
                    value = op.eval_oper(self, self._dl[self._di])
                    if value is not None:
                        # If the operator returned a value, yield it
                        yield value
                    self._di += 1

                elif fun.descr_is_seq(self._dl[self._di]):
                    """Sequence descriptor, replaces current descriptor with expansion"""
                    logger.debug("SEQ %06d", self._dl[self._di])
                    # Current on stack
                    logger.debug("PUSH jump -> *%d %d..%d", len(self._dl), self._di + 1, self._de)
                    stack.append((self._dl, self._di + 1, self._de, "SEQ END"))
                    prevdesc = self._dl[self._di]
                    # Sequence from tabD
                    try:
                        self._dl = self._tables.tab_d[self._dl[self._di]]
                    except KeyError as e:
                        raise BufrDecodeError("Unknown descriptor {}".format(e))
                    # Expansion on stack
                    logger.debug("PUSH seq -> *%d %d..%d", len(self._dl), 0, len(self._dl))
                    stack.append((self._dl, 0, len(self._dl), "SEQ %06d" % prevdesc))
                    # Causes inner while to end
                    self._di = self._de

                else:
                    """Invalid descriptor, out of defined range"""
                    raise BufrDecodeError("Descriptor '%06d' invalid!" % self._dl[self._di])

        self.inprogress = False
        logger.debug("SUBSET END (%s)" % self._blob)
        #raise StopIteration # XXX:
        return

    def eval_loop_descr(self, record=True):
        """Evaluate descriptor for replication/repetition.

        :param record: record element descriptors for delayed replication (if
                        present) in back reference list, default==True.
        :return: amount of descriptors, number of repeats, is_repetition
        """
        # amount of descr
        loop_amnt = self._dl[self._di] // 1000 - 100
        # number of replication
        loop_num = self._dl[self._di] % 1000
        # Repetition?
        is_rep = False
        # Increase di to start-of-loop
        self._di += 1
        if loop_num == 0:
            # Decode next descr for loop-count
            if self._dl[self._di] < 30000 or self._dl[self._di] >= 40000:
                raise BufrDecodeError("No count (031YYY) for delayed loop!")
            try:
                elem_b = self._tables.tab_b[self._dl[self._di]]
            except KeyError as e:
                raise BufrDecodeError("Unknown descriptor {}".format(e))
            loop_num = self.get_val(self._blob,
                                    self.subs_num,
                                    fix_width=elem_b.width)
            if self._as_array:
                if min(loop_num) != max(loop_num):
                    raise BufrDecodeError("Loop-numbers in compression unequal: {}".format(loop_num))
                loop_num = loop_num[0]
            # Descriptors 31011+31012 mean repetition, not replication
            is_rep = 31010 <= elem_b.descr <= 31012
            if record and self._do_backref_record:
                self._backref_record.append(elem_b, None)
            logger.debug("%s %d %d -> %d from %06d",
                         "REPT" if is_rep else "LOOP",
                         loop_amnt, 0, loop_num, elem_b.descr)
            self._di += 1
            if loop_num == 255:
                loop_num = 0
        else:
            logger.debug("LOOP %d %d" % (loop_amnt, loop_num))
        return loop_amnt, loop_num, is_rep

    def _read_refval(self):
        """Set new reference values.

        Reads a set of YYY bits, taking them as new reference values for the
        descriptors of the set. YYY is taken from the current descriptor dl[di],
        reference values are set for all subsequent following descriptors until
        the descriptor signaling the end of operation occurs.

        :return: number of new reference values
        """
        rl = {}
        an = self._dl[self._di] % 1000
        self._di += 1
        while self._di < self._de:
            rval = self.get_val(self._blob,
                                self.subs_num,
                                fix_width=an)
            # Sign=high-bit
            sign = -1 if (1 << (an - 1)) & rval else 1
            # Value=val&(FFF>>1)
            val = ((1 << an) - 1) & rval
            rl[self._dl[self._di]] = sign * val
            self._di += 1
            if self._dl[self._di] > 200000 and self._dl[self._di] % 1000 == 255:
                # YYY==255 is signal-of-end
                break
        self._alter.refval = rl


class SubsetWriter():

    def __init__(self, tables, blob, descr_list, is_compressed, subset_num, edition=4, has_backref=False):
        # Apply internal compression
        self.is_compressed = is_compressed
        # BUFR edition
        self.edition = edition
        # Number of subsets
        self.subs_num = subset_num
        # Holds table object
        self._tables = tables
        # Holds byte array with bufr
        self._blob = blob
        # Initial descriptor list
        self._desc = descr_list
        # End of data for all subsets
        self._data_e = -1
        # Alterator values
        self._alter = AlterState()
        # Skip N data descriptors
        self._skip_data = 0
        # Recording descriptors for back-referencing
        self._do_backref_record = has_backref
        # Recorder for back-referenced descriptors
        self._backref_record = BackrefRecord()
        # Variable names for positioning/current working list in descriptor/value lists:
        # dl : current descriptor list
        # di : index for current descriptor list
        # de : stop when reaching this index
        # vl : values list; compression: list of all subsets, otherwise: one subset's data
        # vi : value list index
        self._dl = []
        self._di = self._de = 0
        self._vl = []
        self._vi = 0
        # Method for writing a value to the bistream, depends on compression
        self.add_val = fun.add_val_comp if self.is_compressed else fun.add_val

    def __str__(self):
        return "Subset #%d/%d, compression:%s" % (self.subs_num, self.is_compressed)

    def process(self, subset_list=[]):
        """ """
        skip_data = False
        # Stack for sequence expansion and loops.
        # Items follow: ([desc,], start, end, mark)
        stack = []
        # Alterator values, this resets them at the beginning of the iterator.
        self._alter = AlterState()
        # Current values list
        self._vl = subset_list
        # Index in current values list
        self._vi = 0
        if not subset_list:
            # On empty subset_list there is nothing to do.
            logger.info("SUBSETS 0 -> empty data section.")
            return
        if self.is_compressed:

            def extract_loop_list(vl, vi):
                """Compression:
                define local function to eval loop count and list of loop lists.
                """
                lst = list(zip(*[x[vi] for x in vl]))
                cnt = len(lst)
                return cnt, lst

            # Put inital descriptor and values list on stack, for compressed BUFR
            # only one is necessary.
            stack.append((self._desc, 0, len(self._desc), subset_list, self._vi))
        else:

            def extract_loop_list(vl, vi):
                """Regular (no compression):
                define local function to eval loop count and list of loop lists.
                """
                lst = vl[vi]
                cnt = len(lst)
                return cnt, lst

            # Put inital descriptor and values list times subset-count on stack
            for vl in subset_list[::-1]:
                stack.append((self._desc, 0, len(self._desc), vl, self._vi))
        while len(stack):
            """Loop while descriptor lists on stack."""
            self._dl, self._di, self._de, sv_l, sv_i = stack.pop()
            if sv_l:
                self._vl, self._vi = sv_l, sv_i
            logger.debug("POP *%d %d..%d *%d #%d", len(self._dl), self._di, self._de, len(self._vl), self._vi)
            while self._di < self._de:
                """Loop over descriptors in current list."""

                if skip_data:
                    """Data not present: data is limited to class 01-09,31."""
                    skip_data -= 1
                    if 1000 <= self._dl[self._di] < 10000 and self._dl[self._di] // 1000 != 31:
                        self._di += 1
                        continue

                if fun.descr_is_nil(self._dl[self._di]):
                    """Null-descriptor to signal end-of-list."""
                    self._di += 1

                elif fun.descr_is_data(self._dl[self._di]):
                    """Element descriptor, decoding bits to value."""
                    logger.debug("ENCODE %06d #%d", self._dl[self._di], self._vi)
                    if self._alter.assoc[-1] and (self._dl[self._di] < 31000 or self._dl[self._di] > 32000):
                        # Associated field with quality information.
                        self.add_val(self._blob, self._vl, self._vi,
                                     fix_width=self._alter.assoc[-1])
                        self._vi += 1
                    try:
                        elem_b = self._tables.tab_b[self._dl[self._di]]
                    except KeyError as e:
                        raise BufrDecodeError("Unknown descriptor {}".format(e))
                    self.add_val(self._blob, self._vl, self._vi, tab_b_elem=elem_b, alter=self._alter)
                    if self._do_backref_record:
                        self._backref_record.append(elem_b, self._alter)
                    self._di += 1
                    self._vi += 1

                elif fun.descr_is_loop(self._dl[self._di]):
                    """Replication/repetition."""
                    loop_cause = self._dl[self._di]
                    # Decode loop-descr:
                    # amount of descr
                    lm = self._dl[self._di] // 1000 - 100
                    # number of replication
                    ln = self._dl[self._di] % 1000
                    # Repetition?
                    is_repetition = False
                    loop_count, loop_lists = extract_loop_list(self._vl, self._vi)
                    # Increase di to start-of-loop
                    self._di += 1
                    if ln == 0:
                        # Decode next descr for loop-count
                        if self._dl[self._di] < 30000 or self._dl[self._di] >= 40000:
                            raise BufrEncodeError("No count for delayed loop!")
                        try:
                            elem_b = self._tables.tab_b[self._dl[self._di]]
                        except KeyError as e:
                            raise BufrDecodeError("Unknown descriptor {}".format(e))
                        self._di += 1
                        self.add_val(self._blob, loop_count or 0, self.subs_num, tab_b_elem=elem_b)
                        # Descriptors 31011+31012 mean repetition, not replication
                        is_repetition = 31010 <= elem_b.descr <= 31012
                        if self._do_backref_record:
                            self._backref_record.append(elem_b, None)
                    logger.debug("%s %d * %d->%d from %06d",
                                 "REPT" if is_repetition else "LOOP",
                                 lm, ln, loop_count, loop_cause)
                    # Current list on stack (di points after looped descr)
                    logger.debug("PUSH jump -> *%d %d..%d *[...],%d",
                                 len(self._dl), self._di + lm, self._de, self._vi + 1)
                    if is_repetition:
                        stack.append((self._dl, self._di + lm, self._de, self._vl, self._vi + 1))
                        if ln:
                            stack.append((self._dl, self._di, self._di + lm, loop_lists[0], 0))
                    else:
                        stack.append((self._dl, self._di + lm, self._de, self._vl, self._vi + 1))
                        for cv_ll in loop_lists[::-1]:
                            # N*list on stack
                            logger.debug("PUSH loop -> *%d %d..%d *%s,%d", len(self._dl),
                                         self._di, self._di + lm, cv_ll, 0)
                            stack.append((self._dl, self._di, self._di + lm, cv_ll, 0))
                            ln -= 1
                    self._di = self._de

                elif fun.descr_is_oper(self._dl[self._di]):
                    """Operator descritor, alter/modify properties."""
                    op.prep_oper(self, self._dl[self._di])
                    self._di += 1

                elif fun.descr_is_seq(self._dl[self._di]):
                    """Sequence descriptor, replaces current descriptor with expansion."""
                    logger.debug("SEQ %06d", self._dl[self._di])
                    # Current on stack
                    logger.debug("PUSH jump -> *%d %d..%d #%d", len(self._dl), self._di + 1, self._de, self._vi)
                    stack.append((self._dl, self._di + 1, self._de, None, None))
                    # Sequence from tabD
                    try:
                        dl = self._tables.tab_d[self._dl[self._di]]
                    except KeyError as e:
                        raise BufrDecodeError("Unknown descriptor {}".format(e))
                    # Expansion on stack
                    logger.debug("PUSH seq -> *%d %d..%d #%d", len(self._dl), 0, len(self._dl), self._vi)
                    stack.append((dl, 0, len(dl), None, None))
                    # Causes inner while to end
                    self._di = self._de

                else:
                    """Invalid descriptor, out of defined range."""
                    raise BufrEncodeError("Descriptor '%06d' invalid!" % self._dl[self._di])

        # Add padding bytes if required
        if self.edition <= 3:
            self._blob.write_align(even=False)
            logger.debug("PADDING -> %d/%d", len(self._blob) // 8, len(self._blob) % 8)

    def _write_refval(self):
        """Set new reference values.

        Writes a set of YYY bits, taking them as new reference values for the
        descriptors of the set. YYY is taken from the current descriptor dl[di],
        reference values are set for all subsequent following descriptors until
        the descriptor signaling the end of operation occurs.

        :return: number of new reference values
        """
        if self.is_compressed:
            lst = [x[self._vi] for x in self._vl]
        else:
            lst = [self._vl[self._vi]]
        rl = {}
        an = self._dl[self._di] % 1000
        self._di += 1
        while self._di < self._de:
            if self._dl[self._di] > 200000 and self._dl[self._di] % 1000 == 255:
                # YYY==255 is signal-of-end
                break
            val = [((1 << an) - 1) & ((1 << (an - 1)) if v < 0 else 0) & v
                   for v in lst]
            rl[self._dl[self._di]] = lst[self._vi]
            self.add_val(self._blob, val, 0, fix_width=an)
            self._di += 1
        self._alter.refval = rl
