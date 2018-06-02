#! python3
# madlibs.py - simple program that searches a text file for keywords and
#              replaces them with user defined alternatives.

import sys
import os
import re


def main():
    try:
        file_to_open = check_arguments()
        check_file_exists(file_to_open)
    except Exception as err:
        sys.stderr.write('ERROR: %s' % str(err))
        return 1
    print_header()
    text_file = get_file_data(file_to_open)
    write_file(text_file)


def get_file_data(file_to_open):
    with open(file_to_open, 'r') as fin:
        data = fin.read()
        fin.close()

    print(data)
    return re.split('(\s|\.)', data)


def write_file(data):
    outdata = ''
    print()
    for i in range(len(data)):
        if data[i] == 'ADJECTIVE':
            print(f'>>> :{outdata} ?')
            data[i] = input("Choose a word to replace ADJECTIVE : ")
        elif data[i] == 'NOUN':
            print(f'>>> :{outdata} ?')
            data[i] = input('Choose a word to replace NOUN : ')
        elif data[i] == 'VERB':
            print(f'>>> :{outdata} ?')
            data[i] = input('Choose a word to replace VERB : ')
        outdata += data[i]
    with open('story_changed', 'w') as fout:
        fout.write(outdata.strip())
        fout.close()
    print('All changes made. Files saved as "story_changed.txt"')

def print_header():
    print('___________________________________________________________________')
    print('___________________M A D L I B S__E D I T O R______________________')
    print('___________________________________________________________________')
    print()


def check_arguments():
    if len(sys.argv) == 1:
        raise RuntimeError('''

No text file supplied as argument...
Please retry using: python3 madlibs.py <textfile>

''')
    elif len(sys.argv) > 2:
        raise RuntimeError('''

Too many arguments supplied...
Please retry using: python3 madlibs.py <textfile>

''')
    else:
        return str(sys.argv[1])


def check_file_exists(filename):
    if not os.path.isfile(filename):
        raise RuntimeError('''

File not found...
Please retry using a valid file

''')


if __name__ == '__main__':
    main()
