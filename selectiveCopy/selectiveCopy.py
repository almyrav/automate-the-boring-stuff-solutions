#!/usr/bin/env python3
#! python3
# selectiveCopy.py - Copies PDF files from one location to another folder.

import os, shutil
           
def move_PDF(folder):
  folder = os.path.abspath(folder) # make sure folder is absolute path
 
  # Make a new directory to place all the PDF files in.
  newFolder = folder + '\PDF'
  if not os.path.isdir(newFolder):
    newFolder = os.mkdir(newFolder)
  
  # Find all PDF files in a folder and its subfolders.
  for foldername, subfolders, filenames in os.walk(os.path.abspath(folder)):
    for filename in filenames:
      if filename.endswith('.pdf') or filename.endswith('.PDF'):
        print('Adding %s to PDF folder.' % (filename))
        fullPathFile = os.path.join(foldername, filename)
        try:
          shutil.copy2(fullPathFile, newFolder)
        except shutil.SameFileError:
          pass
  print('Done.')

def move_JPG(folder):
  folder = os.path.abspath(folder) # make sure folder is absolute path
 
  # Make a new directory to place all the PDF files in.
  newFolder = folder + '\JPG'
  if not os.path.isdir(newFolder):
    newFolder = os.mkdir(newFolder)
  
  # Find all PDF files in a folder and its subfolders.
  for foldername, subfolders, filenames in os.walk(os.path.abspath(folder)):
    for filename in filenames:
      if filename.endswith('.jpg') or filename.endswith('.jpeg'):
        print('Adding %s to images folder.' % (filename))
        fullPathFile = os.path.join(foldername, filename)
        try:
          shutil.copy2(fullPathFile, newFolder)
        except shutil.SameFileError:
          pass
  print('Done.')
move_PDF(os.getcwd())
move_JPG(os.getcwd())
input('Press ENTER to exit...')
