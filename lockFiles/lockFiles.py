#!/usr/bin/env python3
import pikepdf, os, shutil, getpass

# Find all PDF files in a folder and its subfolders.
folder = os.path.abspath(os.getcwd())
securedFolder = 'Secured PDFs'
if not os.path.exists(securedFolder):
    os.makedirs(securedFolder)

userPassword = getpass.getpass("What user password do you want to use? ")
ownerPassword = getpass.getpass("What owner password do you want to use? ")

for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
      if filename.endswith('.pdf') or filename.endswith('.PDF'):
          if os.path.exists(filename):
            print('Adding %s to %s.' % (filename, securedFolder))
            fullPathFile = os.path.join(foldername, filename)
            try:
              my_pdf = pikepdf.Pdf.open(filename)
              
              pdfFilename = os.path.splitext(filename)[0] + ' (Secured).pdf'
              
              my_pdf.save(pdfFilename, encryption=pikepdf.Encryption(user=userPassword, owner=ownerPassword))
              
              shutil.move(pdfFilename, securedFolder)
            except shutil.SameFileError:
              pass
   
    os.chdir('../')  
print('Done.')
    
