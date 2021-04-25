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
          shutil.move(fullPathFile, newFolder)
        except shutil.SameFileError:
          pass
  print('Done.')

def move_JPG(folder):
  folder = os.path.abspath(folder) # make sure folder is absolute path
 
  # Make a new directory to place all the picture files in.
  newFolder = folder + '\JPG'
  if not os.path.isdir(newFolder):
    newFolder = os.mkdir(newFolder)
  
  # Find all picture files in a folder and its subfolders.
  for foldername, subfolders, filenames in os.walk(os.path.abspath(folder)):
    for filename in filenames:
      if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png') or filename.endswith('.jpe'):
        print('Adding %s to images folder.' % (filename))
        fullPathFile = os.path.join(foldername, filename)
        try:
          shutil.move(fullPathFile, newFolder)
        except shutil.SameFileError:
          pass
  print('Done.')
  
def move_Executables(folder):
  folder = os.path.abspath(folder) # make sure folder is absolute path
 
  # Make a new directory to place all the executable files in.
  newFolder = folder + '\Executables'
  if not os.path.isdir(newFolder):
    newFolder = os.mkdir(newFolder)
  
  # Find all executable files in a folder and its subfolders.
  for foldername, subfolders, filenames in os.walk(os.path.abspath(folder)):
    for filename in filenames:
      if filename.endswith('.exe') or filename.endswith('.msi'):
        print('Adding %s to Executables folder.' % (filename))
        fullPathFile = os.path.join(foldername, filename)
        try:
          shutil.move(fullPathFile, newFolder)
        except shutil.SameFileError:
          pass
  print('Done.')
  
def move_Word_Docs(folder):
  folder = os.path.abspath(folder) # make sure folder is absolute path
 
  # Make a new directory to place all the Word files in.
  newFolder = folder + '\Word'
  if not os.path.isdir(newFolder):
    newFolder = os.mkdir(newFolder)
  
  # Find all Word files in a folder and its subfolders.
  for foldername, subfolders, filenames in os.walk(os.path.abspath(folder)):
    for filename in filenames:
      if filename.endswith('.doc') or filename.endswith('.docx'):
        print('Adding %s to Word folder.' % (filename))
        fullPathFile = os.path.join(foldername, filename)
        try:
          shutil.move(fullPathFile, newFolder)
        except shutil.SameFileError:
          pass
  print('Done.')
#move_PDF('C:\\Users\\username\\Downloads')
#move_Executables('C:\\Users\\username\\Downloads')
#move_Word_Docs('C:\\Users\\username\\Downloads')
#move_JPG('C:\\Users\\username\\Pictures')
move_JPG('C:\\Users\\username\\Downloads')
input('Press ENTER to exit...')
