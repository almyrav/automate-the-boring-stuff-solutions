#!/usr/bin/env python3
#! python3
# madlibs.py - Fills in madlib file.

import os, re

def replace_words_string(madlibText):
  replaceRegex = re.compile(r'NOUN|ADJECTIVE|ADVERB|VERB')
  toReplace = replaceRegex.findall(madlibText)
  nounList = ['']
  verbList = ['']
  adjectiveList = ['']
  adverbList = ['']
  for item in range(len(toReplace)):
    if toReplace[item] == 'NOUN':
      print('Enter a noun:')
      nounInput = input()
      nounList.append(nounInput)
    elif toReplace[item] == 'VERB':
      print('Enter a verb:')
      verbInput = input()
      verbList.append(verbInput)
    elif toReplace[item] == 'ADJECTIVE':
      print('Enter an adjective:')
      adjectiveInput = input()
      adjectiveList.append(adjectiveInput)
    elif toReplace[item] == 'ADVERB':
      print('Enter an adverb:')
      adverbInput = input()
      adverbList.append(adverbInput)
  #Nouns
  nounFrags = madlibText.split('NOUN')
  # for noun in range(len(nounFrags)-1):
    # print('Enter a noun:')
    # inputNoun = input()
    # nounList.insert(noun+1, inputNoun)
  for n in range(len(nounFrags)):  
    nounFrags[n] = nounList[n] + nounFrags[n]
  nounMadlibsText = ''.join(nounFrags)
  #Verbs
  verbFrags = re.split('\s+VERB', nounMadlibsText)
  for v in range(len(verbFrags)):
    verbFrags[v] = verbList[v] + verbFrags[v]
  verbMadlibsText = ' '.join(verbFrags)
  #Adjectives
  adjectiveFrags = verbMadlibsText.split('ADJECTIVE')
  for a in range(len(adjectiveFrags)):  
    adjectiveFrags[a] = adjectiveList[a] + adjectiveFrags[a]
  adjectiveMadlibsText = ''.join(adjectiveFrags)
  #Adverbs
  adverbFrags = adjectiveMadlibsText.split('ADVERB')
  for av in range(len(adverbFrags)):  
    adverbFrags[av] = adverbList[av] + adverbFrags[av]
  newMadlibsText = ''.join(adverbFrags)
  return newMadlibsText

while True:  
  # Read text file
  print('Enter the name of the file ([name of file].txt):')
  madlibFileString = input()
  madlibFile = open(madlibFileString + ".txt")
  madlibText = madlibFile.read()
  madlibFile.close()
  
  
  # Write results in new text file
  madlibFileRes = madlibFileString + '_results.txt'
  newMadlibFile = open(madlibFileRes, 'w')
  newText = replace_words_string(madlibText)
  print(newText)
  newMadlibFile.write(newText)
  newMadlibFile.close()


input('Press ENTER to exit...')
