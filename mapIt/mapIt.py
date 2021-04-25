#!/usr/bin/env python3
#! python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.

import webbrowser, sys, pyperclip, logging
logging.basicConfig(filename='mapItLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()
logging.debug('The address is %s' %address)
webbrowser.open('https://www.google.com/maps/place/' + address)
