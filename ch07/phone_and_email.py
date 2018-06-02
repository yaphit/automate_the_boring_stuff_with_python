#! python3
# phone_and_email.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip
import re


phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code followed by ? means it is optional. It can be 3 digits or 3 digits surrounded by ()
    (\s|-|\.)?                      # separator can be a space, hyphen or period. This again is optional
    (\d{3})                         # first 3 digits 
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension is optional. Made up of any number of spaces, followed by either ext, x or ext. and followed by 2 to 5 digits
)''', re.VERBOSE)

# create email regex

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username character 
    @                       # At symbol
    [a-zA-Z0-9.-]+       # domain name
    (\.[a-zA-Z]{2,4})       # dot something
)''', re.VERBOSE)

# find matches in clipboard

text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    print(groups)
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

# copy results onto clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')
