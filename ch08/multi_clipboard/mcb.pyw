#! /usr/bin/env python3
# multi_clipboard.pyw - saves and loads pieces of text to the clipboard.
# Usage: py.exe multi_clipboard.pyw save <keyword> - saves clipboard to keyword.
#        py.exe multi_clipboard.pyw <keyword> - Loads keyword to clipboard.
#        py.exe multi_clipboard.pyw list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('multi_clipboard')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcb_shelf.clear()
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
mcb_shelf.close()
