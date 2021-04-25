#!/usr/bin/env python3
#! python3
#directoryTree.py - Lists all subfolders and files 

import os

for folderName, subfolders, filenames in os.walk(os.getcwd()):
  print('The current folder is ' + folderName)
  for subfolder in subfolders:
    print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
  for filename in filenames:
    print('FILE INSIDE ' + folderName + ': ' + filename)
  
  print('')
input('Press ENTER to exit...')