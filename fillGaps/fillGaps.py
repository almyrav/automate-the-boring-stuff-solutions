#!/usr/bin/env python3
#! python3
#fillGaps.py - Remove gaps in numbered file names.

import os, re, shutil, sys

# Create regex that matches filenames with numbers.
def get_search_term():
  print('\nEnter the numbered file basename:')
  userInput = input()
  numberPattern= re.compile(r'''(''' + userInput + ''')
  (\d+)     #match three digit numbers
  (\.[a-zA-Z]{2,4}) #dot extension
''', re.VERBOSE | re.IGNORECASE)
  return numberPattern

def get_max_length(numberPattern):
  maxLength = 0
  for filename in os.listdir('.'):
    searchRes = numberPattern.search(filename)
    name = os.path.splitext(filename)[0]

    # Skip files that do not match
    if searchRes == None:
      continue

    searchLength = len(name)

    if searchLength > maxLength:
      maxLength = searchLength

  return maxLength

def fill_gaps(numberPattern):
  num = 0
  files = []
  while True:
    numberPattern = get_search_term()
    for filename in os.listdir('.'):
      searchRes = numberPattern.search(filename)
      name = os.path.splitext(filename)[0]
      extension = os.path.splitext(filename)[1]

      maxLength = get_max_length(numberPattern)
      
      # Skip files that do not match
      if searchRes == None:
        continue
      
      inputLength = len(searchRes.group(1))
      fileNum = int(searchRes.group(2))
      numLength = len(str(fileNum))
      
      
      # Figure out the filename this code should use based on what files already exist.
      while fileNum > num + 1:
        fileNum -= 1
        #print(fileNum) #countdown

      name = name[0:inputLength]

      while len(name + str(fileNum)) < maxLength:
        name += '0'
        #print('name: %s' %name)
        
      filename = name + str(fileNum) + extension
      print('Renaming %s to %s...' %(searchRes.group(0),filename))
      #shutil.move(searchRes.group(0), filename)
      #print('num: %d maxLength: %d' % (num, maxLength))
      files.append(searchRes.group(0))
      num = fileNum
      
    if not files:
      print("No files found.")
      print(files)
      
   # Ask if user wants to fill gaps for another file
    print("\nWould you like to fill gaps for another file? Enter 'y' or 'n'.")
    fillAgain = input()
    if fillAgain.casefold() == "y":
      continue
    elif fillAgain.casefold() == "n": 
      print("\nGoodbye")
      input("Press ENTER to exit...")
      sys.exit()
    else:
      print("\nPlease enter 'y' or 'n'.")
numberPattern = 0
fill_gaps(numberPattern)

input('Press ENTER to exit...')
