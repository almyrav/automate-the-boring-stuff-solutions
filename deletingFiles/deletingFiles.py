#!/usr/bin/env python3
#! python3
#deletingFiles.py - Show files larger than 100MB.

import os
def show_file_sizes(folder):
  folder = os.path.abspath(folder) # make sure folder is absolute path
  
  # Find all files in a folder and its subfolders.
  for foldername, subfolders, filenames in os.walk(os.path.abspath(folder)):
    for filename in filenames:
      #os.path.getsize(path) - returns file size in bytes
      fullPathFile = os.path.join(foldername, filename)
      # Print files that are greater than 100MB.
      if os.path.getsize(fullPathFile) > 1000000 * 100:  
        print(filename + ': ' + str(os.path.getsize(fullPathFile)/1000000) + 'MB\n' + fullPathFile)

  print('Done.')
show_file_sizes('insert folder path here')
input('Press ENTER to exit...')