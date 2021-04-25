#!/usr/bin/env python3
#! python3
#extractAllZip.py - Extracts all archive files

import zipfile, os, sys, shutil, rarfile
    
def extractAllZip():
  # Extract all archive files in current folder.

    currentDirName = os.getcwd()
  
    # Specify folder  
    print("\nPress 'ENTER' on your keyboard to extract all the archives in '%s':" % (currentDirName))
    extractAll = input()
    
    # If user pressed "ENTER", the folderExists() function will test the current directory and the rootFolder will be the absolute path of the current folder for the os.walk() function
    if extractAll == "":
    
      for filename in os.listdir(currentDirName):

          if not filename.endswith('.rar') and not filename.endswith('.zip'):
              continue
          
          if zipfile.is_zipfile(filename) and filename.endswith('.zip'):
            with zipfile.ZipFile(filename, 'r') as myzip:
              #myzip.extractall()
              print('Extracting %s to %s' % (filename, currentDirName))
          elif rarfile.is_rarfile(filename) and filename.endswith('.rar'):
              with rarfile.RarFile(filename) as myrar:
                myrar.extractall()
                print('Extracting %s to %s' % (filename, currentDirName))
          
      print('Done.')
      input("Press ENTER to exit...")
    else:
      input("Press ENTER to exit...")
      
extractAllZip()

