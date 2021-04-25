#!/usr/bin/env python3
#! python3
##Insecure Password Manager

import sys, pyperclip, re

PASSWORDS = {'neopets': '784hker4JYDK9Hk',
             'runescape': 'IUDjuiu8792jIUHuyhk',
             'account': 'password'}

if len(sys.argv) < 2:
    print("Usage:\npw.py [account] - copy account password\npw.py [account] strength - check strength of password")
    input("Press ENTER to exit...")

account = sys.argv[1] #first command line arg is the account number  

#optional second command line argument
try:
  passStrength = sys.argv[2]
except IndexError:
  passStrength = None

def isLong(password):
  longPassRegex = re.compile(r'(.){8,}')
  longPass = longPassRegex.search(password)
  if longPass is None:
    return False
  else:
    return True

def hasNum(password):
  numPassRegex = re.compile(r'\d')
  numPass = numPassRegex.search(password)
  if numPass is None:
    return False
  else:
    return True

def hasMixCap(password):
  lowerCapRegex = re.compile(r'[a-z]')
  lowerCap = lowerCapRegex.search(password)
  upperCapRegex = re.compile(r'[A-Z]')
  upperCap = upperCapRegex.search(password)
  if lowerCap is None or upperCap is None:
    return False
  else:
    return True
    
def hasChar(password):
  hasCharRegex = re.compile(r'\D\W\S')
  hasChar = hasCharRegex.search(password)
  if hasChar is None:
    return False
  else:
    return True

def checkStrength(password, account):
  pStrength = ""
  if(isLong(password) and not hasNum(password) and hasMixCap(password) and not hasChar(password))or(not isLong(password) and hasNum(password) and hasMixCap(password) and not hasChar(password))or(isLong(password) and hasNum(password) and not hasMixCap(password) and not hasChar(password)):
    pStrength = "moderate"
  elif isLong(password) and hasNum(password) and hasMixCap(password) and not hasChar(password):
    pStrength = "strong"
  elif isLong(password) and hasNum(password) and hasMixCap(password) and hasChar(password):
    pStrength = "very strong"
  else:
    pStrength = "weak"
  print("Passwords can be:\nWeak\nModerate\nStrong\nVery Strong\nPassword strength for " + account +": " + pStrength)
  
if account in PASSWORDS:
    password = PASSWORDS[account]
    if passStrength == "strength":
      checkStrength(password, account)
    else:
      pyperclip.copy(password)
      print("Password for " + account + " copied to clipboard.")
else:
    print("There is no account named " + account + ".")
 
input("Press ENTER to exit...")