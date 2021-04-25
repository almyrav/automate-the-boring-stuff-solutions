#!/usr/bin/env python3
#! python3
# regexSearch.py - Finds a user input regex search term from all the text files in the current directory.

import os, re, sys

def search_term():
  print('Enter a regex search term:')
  userInput = input()
  searchRegex = re.compile(r'''(''' + userInput + ''')''', re.VERBOSE)
  return searchRegex
def find_text(search_term):
  fileMatches = []

  for fileName in os.listdir(os.getcwd()):
    if fileName.endswith('.txt'): 
      fileMatches.append(fileName)
      fileFullPath = os.path.join(os.getcwd(), fileName)
      textFile = open(fileFullPath)
      text = textFile.readlines()
      textStrPre = ''.join(text)
      puncRegex = re.compile('[.?!]')
      puncList = puncRegex.findall(textStrPre)
      textList = []
      for line in range(len(text)):
        for punc in puncList:
          if punc in text[line]:
            sentence = text[line].split(punc)
            for s in sentence:
              textList.append(s + punc + ' BREAK ')
            break
        else:
          #Divide string with no punctuation into 50 characters
          sentence = text[line]
          b=0
          for i in range(len(sentence)):
            if i%50 == 0:
              textList.append(sentence[b:i] + ' BREAK ')
              b=i
        continue
      textStr = ''.join(textList)
      #search
      splitText = re.split(' BREAK |\n', textStr)
      searchList = searchRegex.findall(textStr)
      if searchList != []:
        print('\n\n' + os.path.join(os.getcwd(), fileName))
        for phraseNum in range(len(splitText)):
          searchListText = searchRegex.findall(splitText[phraseNum])
          if searchListText != []:
            print('\nSentence ' + str(phraseNum+1) + ': ' + splitText[phraseNum])
            words = re.split('\s', splitText[phraseNum])
            print('Match: ', end = '')
            for word in words:
              wordMatch = searchRegex.search(word)
              if wordMatch != None:
                print(word, end = ' ')
      else:
        print('\n\n' + os.path.join(os.getcwd(), fileName))
        print('\nNo matches found.')
      textFile.close()
  if fileMatches == []:
    print('No text files found.')
searchRegex = search_term()
find_text(searchRegex)
while True:
  print("\nWould you like to try again? Enter 'y' or 'n'.")
  tryAgain = input()
  if tryAgain.casefold() == "y":
    searchRegex = search_term()
    find_text(searchRegex)
  elif tryAgain.casefold() == "n": 
    print("\nGoodbye")
    input("Press ENTER to exit...")
    sys.exit()
  else:
    print("\nPlease enter 'y' or 'n'.")