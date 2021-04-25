#!/usr/bin/env python3
#! python3

import sys, re

if len(sys.argv) < 2:
  print("Usage:\nregStrip.py [text] - remove trailing whitespace from text\nregStrip.py [text] [characters] - remove characters from text")
  input("Press ENTER to exit...")

def removeChars(text,remove):
  charRegex = re.compile(r'[^' + remove + ']')
  findChars = charRegex.findall(text)
  print("".join(findChars))
  
def removeSpace(text):
  spaceRegex = re.compile(r'\S')
  findSpace = spaceRegex.findall(text)
  print("".join(findSpace))
  
text = sys.argv[1]

try:
  remove = sys.argv[2]
except IndexError:
  remove = None
  
if remove is None:
  removeSpace(text)
else:
  removeChars(text, remove)
input("Press ENTER to exit...")