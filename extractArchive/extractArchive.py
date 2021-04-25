#!/usr/bin/env python3
#! python3
#extractArchive.py - Extracts specified archive

import zipfile, os, sys, shutil, rarfile, re
    
# List directories inside the current working directory
def listDirs(currentDirName):
  print("Here are the archive folders in '%s':" % (currentDirName))
  for filename in os.listdir(currentDirName):

      if not filename.endswith('.rar') and not filename.endswith('.zip'):
          continue
      print(filename)  

# Create regex that matches filenames with numbers.
def get_search_term():
  print('\nEnter file name:')
  userInput = input()
  numberPattern= re.compile(r'''(''' + userInput + ''')
  (\.[a-zA-Z]{3,4}) #dot extension
''', re.VERBOSE | re.IGNORECASE)
  return numberPattern

def extractArchive():

    currentDirName = os.getcwd()
    
    while True:
      listDirs(currentDirName)    
      
      # Specify folder  
      print("\nWhich folder would you like to extract in '%s':" % (currentDirName))
      numberPattern = get_search_term()
      
      for filename in os.listdir(currentDirName):
          searchRes = numberPattern.search(filename)

          # Skip files that do not match
          if searchRes == None:
            continue
          
          if not filename.endswith('.rar') and not filename.endswith('.zip'):
              continue
          
          if zipfile.is_zipfile(filename) and filename.endswith('.zip'):
            with zipfile.ZipFile(filename, 'r') as myzip:
              #myzip.extractall()
              print('Extracting %s to %s' % (filename, currentDirName))
          elif rarfile.is_rarfile(filename) and filename.endswith('.rar'):
              with rarfile.RarFile(filename) as myrar:
                #myrar.extractall()
                print('Extracting %s to %s' % (filename, currentDirName))
            

      # Ask if user wants to fill gaps for another file
      print("\nWould you like to extract another file? Enter 'y' or 'n'.")
      fillAgain = input()
      if fillAgain.casefold() == "y":
        continue
      elif fillAgain.casefold() == "n": 
        print("\nGoodbye")
        input("Press ENTER to exit...")
        sys.exit()
      else:
        print("\nPlease enter 'y' or 'n'.")      
extractArchive()

