#!/usr/bin/env python3
#! python3
#makeSampleFolders.py - Make folders for python scripts

import os, shutil, logging
logging.basicConfig(filename='makeSampleFoldersLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.py') and not os.path.isdir(os.path.splitext(filename)[0]) and os.path.splitext(filename)[0] != 'makeSampleFolders':
        logging.debug('\nfile: %s' % (os.path.splitext(filename)[0]))
        os.makedirs(os.path.splitext(filename)[0])
        shutil.move(filename,os.path.splitext(filename)[0])
    else:
        logging.debug('Skipping %s' %filename)
