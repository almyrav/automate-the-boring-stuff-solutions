#!/usr/bin/env python3
#! python3
# downloadIt.py - Download a web page

import requests, bs4, sys, pyperclip, shutil, logging
logging.basicConfig(handlers=[logging.FileHandler('downloadItLog.txt', 'w', 'utf-8')], level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


url = pyperclip.paste()
logging.debug('The url is %s' %url)

# Download web page
res = requests.get(url)
print('Downloading...')
res.raise_for_status()

# Write contents to a file
file = open('contents.html', 'wb')
for chunk in res.iter_content(100000):
    file.write(chunk)
file.close()

fileSoup = bs4.BeautifulSoup(open('contents.html'), features="lxml")

elems = fileSoup.select('.programlisting')
logging.info('Type of elements: %s' % type(elems))
logging.info('Number of elements: %d' % len(elems))
logging.info('Type of element: %s' % type(elems[0]))
logging.info('Attributes of element: %s' % elems[0].attrs)

contentsList = []
for elem in elems:
    contentsList.append(elem.getText())
    logging.debug('elem: %s' %elem.getText())
contentsList.insert(0, 'Code snippets:')
contentsStr = '\n\nSnippet:\n'.join(contentsList)

contents = open('contents.txt', 'w', encoding='utf-8')
contents.write(contentsStr)
contents.close()






