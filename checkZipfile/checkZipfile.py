#!/usr/bin/env python3
#! python3
# checkZipfile.py - Check size of compressed file in a zip file
import zipfile, os, logging
logging.basicConfig(filename='checkZipfileLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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


  
def check_compressed_file():
    #logging.disable(logging.CRITICAL)
    while True:
        listDirs()

        # Specify folder  
        print("\nEnter the name of a zip file in '%s':" % (currentDirName))
        folderInput = input()

        # Test whether typed folder name is in current working directory or not
        # If not, ask user to continue or exit the program
        if folderExists(folderInput) == False:
          print("%s.zip does not exist. Would you like to try again? Enter 'y' or 'n'." %folderInput)
          tryAgain = input()
          if tryAgain.casefold() == "y":
            continue
          elif tryAgain.casefold() == "n": 
            print("\nGoodbye")
            input("Press ENTER to exit...")
            sys.exit()
          else:
            print("\nPlease enter 'y' or 'n'.")

        zipFolder = zipfile.ZipFile(folderInput + '.zip')
        zipFolder.namelist()
        fileInfo = zipFolder.getinfo('spam.txt')
        fileInfo.file_size
        fileInfo.compress_size
        'Compressed file is %sx smaller!' % (round(fileInfo.file_size / fileInfo
        .compress_size, 2))
        zipFolder.close()
        print("Done")

        # Ask if user wants to do another file
        print("\nWould you like to check another file? Enter 'y' or 'n'.")
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
check_compressed_file()
