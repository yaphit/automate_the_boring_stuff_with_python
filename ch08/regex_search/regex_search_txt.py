#! python3
#  regex_search_txt.py
#  search all text files within a folder for regular expression


import os
import sys
import re

def main():
    print_header()
    find_folder(os.getcwd())
    expression = get_regex(os.getcwd())
    search_files(expression)


def print_header():
    print('___________________________________________________________________')
    print('___________________R E G E X__S E A R C H__________________________')
    print('___________________________________________________________________')
    print()


def find_folder(cwd):
    files_and_directories = os.listdir(cwd)
    dir_options = show_directories(files_and_directories)

    while True:
        print()
        dir_number = int(input(f'Choose directory to search by typing number... '))
        try:
            os.chdir(dir_options[dir_number - 1])
            break
        except:
            print('Error, please enter the number of the directory you wish to search')
            print()
    return


def show_directories(location):
    loc_location = []
    for i in range(0, len(location)):
        if os.path.isdir(location[i]):
            loc_location.append(location[i])
    if not loc_location:
        print("No local directory")
        sys.exit(0)
    print()
    print('Found local directories...')
    for i, file in enumerate(loc_location):
        print()
        print(f'    {i+1} = {loc_location[i]}')
    return loc_location


def get_regex(location):
    print(f'The parent directory is {location}')
    print()
    show_files(os.listdir(location))
    print()
    while True:
        regex = input('Enter a regular expression to search for inside all txt files')
        if regex:
            break
    return re.compile(regex)


def show_files(location):
    loc_location = []
    for i in range(0, len(location)):
        if os.path.isfile(location[i]):
            loc_location.append(location[i])
    if not loc_location:
        print("No files in directory")
        sys.exit(0)
    print('Found local files...')
    print()
    for file in range(len(loc_location)):
        print(f'    {loc_location[file]}')


def search_files(regex):
    files = os.listdir(os.getcwd())
    for i in range(0, len(files)):
        with open(files[i], 'r', encoding='utf-8') as fin:
            line_num = 0
            for line in fin:
                line_num += 1
                if regex.search(line):
                    print(files[i], line_num, line)


if __name__ == '__main__':
    main()
