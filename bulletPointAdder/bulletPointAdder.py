#!/usr/bin/env python3
#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip, logging
logging.basicConfig(filename='bulletPointAdderLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#logging.disable(logging.CRITICAL)
logging.info("Program started")
text = pyperclip.paste()


#Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): #loop through all indexes in the "lines"
    lines[i] = '* ' + lines[i] #add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
logging.debug("Text on the clipboard: \n'%s'" %text)
logging.info("Program ended")
