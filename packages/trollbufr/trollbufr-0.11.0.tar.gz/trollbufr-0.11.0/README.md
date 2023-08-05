# trollBUFR
A pure pythonic reader/writer for BUFR, the meteorological
"Binary Universal Format for data Representation"

_(C) 2016-2018 Alexander Maul_

## Read-the-docs
[http://trollbufr.readthedocs.io](http://trollbufr.readthedocs.io/)

## BUFR-Tables
TDCF table sets are provided as ZIP-archives in different formats, or go to:
* [ECMWF eccodes](https://software.ecmwf.int/wiki/display/ECC/ecCodes+Home).
* [DWD's OpenData server](https://opendata.dwd.de/weather/lib/bufr/).

If files `operator.table` and/or `datacat.table` are not present in your table
directory, there are standard ones in this project's root.
These files are not required for decoding, but optional for readable output.

## Command-line program "trollbufr"
Command-line interface created by setup-py.

* It reads BUFR (with abbreviated heading line, if present) from file(s) and
  writes human-readable to stdout.
* Decoding to JSON-formated file.
* Encoding JSON-formated values to BUFR.

## News
`Vers. 0.10.0`
All code supports Python2 *and* Python3, without code-conversion (i.e. by 2to3).

With Python3 the `setup.py` installs the command-line script with a different
name `trollbufr3`, to reflect its usage of Python3 and to have both versions
callable.

`Vers. 0.6.0`
With version 0.6.0 a feature for encoding a JSON formatted file into binary BUFR
is added.

The command-line options are changed:

* print information and descriptor sections: `-d` became `-m`.
* decode BUFR: `-r` became `-d`.

New is `-j` to write any output in a JSON format.

## To-Do
There are still things to do:

* Implement the remaining obscure operators
