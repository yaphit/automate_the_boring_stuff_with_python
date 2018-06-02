import re
import pyperclip

DateRegex = re.compile(r'''(
    (\d|\d\d|\d{4})
    (-|/)
    (\d\d)
    (-|/) 
    (\d|\d\d|\d{4})   
)''', re.VERBOSE)

matches = []
text = str(pyperclip.paste())

for groups in DateRegex.findall(text):
    if len(groups[1]) == 2:
        dates = '/'.join([groups[1], groups[3], groups[5]])
    else:
        dates = '/'.join([groups[5], groups[3], groups[1]])
    matches.append(dates)


# copy results onto clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No dates found')
