#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Alexander Maul
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

'''
Created on Sep 15, 2016

@author: amaul
'''
from .bufr_types import TabBType, DescrInfoEntry

import logging
logger = logging.getLogger("trollbufr")


class Tables(object):
    '''
    classdocs
    '''
    # Master table
    _master = 0
    # Version master table
    _vers_master = 0
    # Version local table
    _vers_local = 0
    # Centre
    _centre = 0
    # Sub-centre
    _centre_sub = 0

    def __init__(self, master=0, master_vers=0, local_vers=0, centre=0, subcentre=0):
        '''Constructor'''
        self._master = master
        self._vers_master = master_vers
        self._vers_local = local_vers
        self._centre = centre
        self._centre_sub = subcentre
        # { code -> meaning }
        self.tab_a = dict()
        # { desc -> TabBElem }
        self.tab_b = dict()
        # { desc -> (name, definition) }
        self.tab_c = dict()
        # { desc -> (desc, ...) }
        self.tab_d = dict()
        # { desc -> {num:value} }
        self.tab_cf = dict()

    def differs(self, master, master_vers, local_vers, centre, subcentre):
        """Test if the version etc. numbers differ from the table currently loaded"""
        return (self._master != master or self._vers_master != master_vers or
                self._vers_local != local_vers or self._centre != centre or
                self._centre_sub != subcentre)

    def lookup_codeflag(self, descr, val):
        """Interprets value val according the code/flag tables.

        Returns val if it's not of type code table or flag table.
        """
        sval = val
        if not isinstance(descr, int):
            descr = int(descr)
        if descr < 100000:
            b = self.tab_b[descr]
            if self.tab_cf.get(descr) is None:
                return sval
            if b.typ == TabBType.CODE:
                sval = self.tab_cf[descr].get(val)
                logger.debug("CODE %06d: %d -> %s", descr, val, sval)
            elif b.typ == TabBType.FLAG:
                vl = []
                for k, v in list(self.tab_cf[descr].items()):
                    if val & (1 << (b.width - k)):
                        vl.append(v)
                sval = "|".join(vl)
                logger.debug("FLAG %06d: %d -> %s", descr, val, sval)
        return sval or "N/A"

    def lookup_elem(self, descr):
        """Returns name, short-name, unit, and type in a named tuple
        associated with table B or C descriptor.
        """
        if descr < 100000:
            b = self.tab_b.get(descr)
            if b is None:
                return DescrInfoEntry("UNKN", None, "", None)
            return DescrInfoEntry(b.full_name, b.abbrev, b.unit, b.typ)
        elif 200000 < descr < 300000:
            if descr in self.tab_c:
                c = self.tab_c.get(descr)
            else:
                c = self.tab_c.get(descr // 1000)
            if c is None:
                return DescrInfoEntry("UNKN", None, "", "oper")
            return DescrInfoEntry(c[0], None, "", "oper")
        else:
            return DescrInfoEntry(None, None, None, None)

    def lookup_common(self, val):
        """Returns meaning for data category value."""
        a = self.tab_a.get(val)
        logger.debug("COMMONS %d -> %s", val, a)
        return a or "UNKN"


class TabBElem(object):

    def __init__(self, descr, typ_str, unit, abbrev, full_name, scale, refval, width):
        type_list = {"A": TabBType.STRING,
                     "N": TabBType.NUMERIC,
                     "C": TabBType.CODE,
                     "F": TabBType.FLAG,
                     "long": TabBType.LONG,
                     "double": TabBType.DOUBLE,
                     "code": TabBType.CODE,
                     "flag": TabBType.FLAG,
                     "string": TabBType.STRING}
        self.descr = descr
        self.typ = type_list.get(typ_str, None)
        if self.typ == TabBType.NUMERIC:
            if scale > 0:
                self.typ = TabBType.DOUBLE
            else:
                self.typ = TabBType.LONG
        elif self.typ is None:
            raise BaseException("Invalid entry typ_str '%s'" % typ_str)
        self.unit = unit
        self.abbrev = abbrev
        self.full_name = full_name
        self.scale = scale
        self.refval = refval
        self.width = width

    def __str__(self):
        if isinstance(self.descr, int):
            return "%06d : '%s' (%s) [%s]" % (self.descr, self.full_name, self.typ, self.unit)
        else:
            return "%s : '%s' (%s) [%s]" % (self.descr, self.full_name, self.typ, self.unit)
