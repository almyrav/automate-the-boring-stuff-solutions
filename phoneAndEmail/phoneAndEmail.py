#!/usr/bin/env python3
#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re, sys

phoneRegex = re.compile(r'''(
  (\d{3}|\(\d{3}\))?
  (\s|-|\.)?
  (\d{3})
  (\s|-|\.)
  (\d{4})
  (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
  [a-zA-Z0-9._%+-]+      # username
  @                      # @ symbol
  [a-zA-Z0-9.-]+         # domain name
  (\.[a-zA-Z])*
  (\.[a-zA-Z]{2,4})      # dot-something
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
  phoneNum = '-'.join([groups[1], groups[3], groups[5]])
  if groups[8] != '':
    phoneNum += ' x' + groups[8]
  matches.append(phoneNum)
for groups in emailRegex.findall(text):
  emailAddress = ''.join(groups[0])
  matches.append(emailAddress)

if len(matches) > 0:
  matchesString = '\n'.join(matches)
  print(matchesString)
  while True:  
    print("Would you like to copy to clipboard? Enter 'y' or 'n'")
    copyMatch = input()
    if copyMatch.casefold() == 'y':
        break;
    elif copyMatch.casefold() == 'n':
        input("Type ENTER to exit...")
        sys.exit()
    else:
        print("Please enter 'y' or 'n'")
  pyperclip.copy(matchesString)
  print('Copied to clipboard:')
  print(matchesString)
  input("Type ENTER to exit...")
else:
  print('No phone number or email addresses found.')
  input("Type ENTER to exit...")