#!/usr/bin/env python3
#! python3
#backupToZip.py - Copies an entire folder and its contents into a ZIP file whose filename increments.

import zipfile, os, sys, shutil, logging
logging.basicConfig(filename='backupToZipLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

currentDirName = os.path.basename(os.getcwd())

# List directories inside the current working directory
def listDirs():
  print("Here are the folders in '%s':" % (currentDirName))
  for root, dirs, files in os.walk(os.getcwd()):
      for dir in dirs:
        if os.path.isdir(dir):
          print(dir)

# Check if folder is in current directory
def folderExists(folderName):
  if not os.path.isdir(folderName):
    print("The folder '%s' does not exist in '%s'." % (folderName, currentDirName))
    return False
    
def backupToZip():
  #logging.disable(logging.CRITICAL)
  while True:
      listDirs()
    # Backup the entire contents of 'folder' into a ZIP file. 
      # Specify folder  
      print("\nPress 'ENTER' on your keyboard to make a backup of the current folder '%s'\nor \nenter the name of a folder in '%s':" % (currentDirName, currentDirName))
      folderInput = input()
      
      folder = os.path.abspath(folderInput) # make sure folder is absolute
      
      # Value of rootFolder variable depends on whether the user pressed "ENTER" on the keyboard or typed a folder name
      # If user typed a folder name, the folderExists() function will test the folders inside the current directory and the rootFolder will use the relative path of the typed folder name for the os.walk() function
      rootFolder = os.path.basename(folder)
      # If user pressed "ENTER", the folderExists() function will test the current directory and the rootFolder will be the absolute path of the current folder for the os.walk() function
      if folderInput == "":
        folderInput = os.getcwd()
        os.chdir('../')
        rootFolder = os.path.basename(folderInput)
        
        
      
      # Test whether typed folder name is in current working directory or not
      # If not, ask user to continue or exit the program
      if folderExists(folderInput) == False:
        print("Would you like to try again? Enter 'y' or 'n'.")
        tryAgain = input()
        if tryAgain.casefold() == "y":
          continue
        elif tryAgain.casefold() == "n": 
          print("\nGoodbye")
          input("Press ENTER to exit...")
          sys.exit()
        else:
          print("\nPlease enter 'y' or 'n'.")
          
      # Figure out the filename this code should use based on what files already exist.
      number = 1
      while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
          break
        number = number + 1
        logging.debug(str(number))
        
      # Create the ZIP file.
      print('Creating %s...' % (zipFilename))
      backupZip = zipfile.ZipFile(zipFilename, 'w', zipfile.ZIP_DEFLATED)
      
      
      # Walk the entire folder tree and compress the files in each folder.
      for foldername, subfolders, filenames in os.walk(rootFolder):
        logging.debug('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
          newBase=os.path.basename(folder) + '_'
          if filename.startswith(newBase) and filename.endswith('.zip'):
            continue   # don't backup the backup ZIP files
          backupZip.write(os.path.join(foldername, filename))
      backupZip.close()
      if currentDirName == os.path.basename(folderInput):
        logging.debug("folderInput: %r currentDirName: %s" % (os.path.basename(folderInput), currentDirName))
        os.chdir(os.path.abspath(currentDirName))
      print(currentDirName)          
      print('Done.')
      
      # Ask if user wants another backup
      print("\nWould you like to make another backup folder? Enter 'y' or 'n'.")
      zipAgain = input()
      if zipAgain.casefold() == "y":
        continue
      elif zipAgain.casefold() == "n": 
        print("\nGoodbye")
        input("Press ENTER to exit...")
        logging.info("Exit program")
        sys.exit()
      else:
        print("\nPlease enter 'y' or 'n'.")
backupToZip()
