#! python3
# rename_dates.py - Renames filenames with American style MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil
import os
import re


def main():
    american_date_regex = re.compile(r'''^(.*?) # all text before the date note: ^ matches start of line.
        ((0|1)?\d)-                             # one or two digits for the month
        ((0|1|2|3)?\d)-                         # one or two digits for the day
        ((19|20)\d\d)                           # four digits for the year
        (.*?)$                                  # all text after the date note: $ matches end of line
        ''', re.VERBOSE)

    for amer_filename in os.listdir('.'):
        mo = american_date_regex.search(amer_filename)

        if mo == None:
            continue

        before_part = mo.group(1)
        month_part = mo.group(2)
        day_part = mo.group(3)
        year_part = mo.group(4)
        after_part = mo.group(5)

        euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

        abs_work_dir = os.path.abspath('.')
        amer_filename = os.path.join(abs_work_dir, amer_filename)
        euro_filename = os.path.join(abs_work_dir, euro_filename)

        print(f'Renaming {amer_filename} to {euro_filename}...')
        shutil.move(amer_filename, euro_filename)


if __name__ == '__main__':
    main()
