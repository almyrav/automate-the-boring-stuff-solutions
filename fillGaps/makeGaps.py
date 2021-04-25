#!/usr/bin/env python3
#! python3
#makeGaps.py - make gaps in numbered file names.

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

def list_files():
  for filename in os.listdir('.'):
    print(filename)

def make_gaps(numberPattern):
  num = 0
  files = []
  while True:
    list_files()
    numberPattern = get_search_term()
    print("After which file do you want to add a gap?")
    gapNumber = int(input())
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
      if fileNum <= gapNumber:
        num = fileNum + 1
        #print('fileNum1:%d num1: %d' % (fileNum, num))
        continue
      

      if fileNum == num:
        #print('fileNum:%d num: %d' % (fileNum, num))
        fileNum += 1
        num += 1
        #print('fileNum2:%d num2: %d' % (fileNum, num))
      else:
        break
        #print(fileNum) 

      name = name[0:inputLength]

      while len(name + str(fileNum)) < maxLength:
        name += '0'
        #print('name: %s' %name)
        
      filename = name + str(fileNum) + extension
      print('Renaming %s to %s...' %(searchRes.group(0),filename))
      #shutil.move(searchRes.group(0), filename)
      #print('fileNum: %d num: %d' % (fileNum, num))
      files.append(searchRes.group(0))
      
    if not files:
      print("No files found.")
      
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
make_gaps(numberPattern)

input('Press ENTER to exit...')
