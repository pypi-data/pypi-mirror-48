PLTable
=======

PLTable is a Python library designed to make it quick and easy to represent tabular data in visually appealing ASCII tables. PLTable is a fork of [PTable](https://github.com/kxxoling/PTable) which was in turn originally forked from [PrettyTable](https://github.com/lmaurits/prettytable) :

- [PrettyTable by Luke Maurits](https://github.com/lmaurits/prettytable)
  - [PTable by Kane Blueriver](https://github.com/kxxoling/PTable)
    - [PTable by Ryan James](https://github.com/Autoplectic/PTable/tree/boxchar)
      - [PLTable by Plato Mavropoulos](https://github.com/platomav/PLTable)

Compared to PTable, PLTable:

- Adds table style "UNICODE_LINES" based on Ryan James's original line drawing mode at PTable boxchar branch.
- Adds JSON Dictionary export via "get_json_dict" method. Convert it to JSON via python's built-in json import.
- Fixes HTML export via "get_html_strin" by adding proper table Title/Caption and valid xHTML parameter toggle.

You can find the full PrettyTable documentation at the [PTable](https://ptable.readthedocs.io/en/latest/) or [PrettyTable](https://code.google.com/archive/p/prettytable/wikis) wikis.

To install PLTable, use pip via **pip install PLTable** or build from source via **python setup.py install**.