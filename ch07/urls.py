import pyperclip
import re

#todo: create regex object

UrlAddress = re.compile(r'((http://|https://)(www)(.)(\w*)(.)(\D{2,3}))')
# copy clipboard and search
text = str(pyperclip.paste())
matches = []
for groups in UrlAddress.findall(text):
    matches.append(groups[0])
# provide output
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No url addresses found')