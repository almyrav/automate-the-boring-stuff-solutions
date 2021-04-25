#!/usr/bin/env python3
import pikepdf, os, shutil, getpass

# Find all PDF files in a folder and its subfolders.
folder = os.path.abspath(os.getcwd())
unsecuredFolder = 'Unlocked PDFs'
if not os.path.exists(unsecuredFolder):
    os.makedirs(unsecuredFolder)

userPassword = getpass.getpass("User password: ")
#ownerPassword = getpass.getpass("What owner password do you want to use? ")

for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
      if filename.endswith('.pdf') or filename.endswith('.PDF'):
          if os.path.exists(filename):
            print('unlocking %s...' % (filename))
            fullPathFile = os.path.join(foldername, filename)
            try:
              my_pdf = pikepdf.Pdf.open(filename, password=userPassword)
              
              pdfFilename = os.path.splitext(filename)[0][0:-9] + '.pdf'
              
              my_pdf.save(pdfFilename)
              
              shutil.move(pdfFilename, unsecuredFolder)
            except shutil.SameFileError:
              pass
   
    os.chdir('../')  
print('Done.')
    
