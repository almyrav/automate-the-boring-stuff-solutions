#!/usr/bin/env python3
#! python3
# downloadIt.py - Download a web page

import bs4
import logging
import pyperclip
import re
import requests

logging.disable()


# logging.basicConfig(handlers=[logging.FileHandler('downloadItLog.txt', 'w', 'utf-8')], level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def get_regex_line(line):
    line = ' '.join(line)
    #    if re.search(r'(?<!^)(\w+|\d+)([A-Z].*)+,\s([A-Z]{2})\s(\d+)$', line):
    #        line = re.sub(r'(?<!^)(\w+|\d+)([A-Z].*)+,\s([A-Z]{2})\s(\d+)$', r'\1\n\2\n\3\n\4', line)
    if re.search(r'(?<!^)(\w+|\d+)\s(\d+)([A-Z].*)+,\s([A-Z]{2})\s(\d+)$', line):
        line = re.sub(r'(?<!^)(\w+|\d+)\s(\d+)([A-Z].*)+,\s([A-Z]{2})\s(\d+)$', r'\1 \2\n\3\n\4\n\5', line)
    elif re.search(r'(?<!^)(\w+|\d+)([A-Z].*)+,\s([A-Z]{2})\s(\d+\b)\s([A-Za-z]+)+', line):
        line = re.sub(r'(?<!^)(\w+|\d+)([A-Z].*)+,\s([A-Z]{2})\s(\d+\b)\s([A-Za-z]+)+', r'\1\n\2\n\3\n\4\n\5', line)
    elif re.search(r'(?<!^)(\w+|\d+)([A-Z].*)+\s(\w+|\d+)([A-Z].*)+,\s([A-Z]{2})\s(\d+)$', line):
        line = re.sub(r'(?<!^)(\w+|\d+)([A-Z].*)+\s(\w+|\d+)([A-Z].*)+,\s([A-Z]{2})\s(\d+)$', r'\1 \2 \3\n\4\n\5\n\6',
                      line)
    elif re.search(r'(?<!^)(\w+|\d+)([A-Z].*)+\s(\w+|\d+)([A-Z].*)+,\s([A-Z]{2})\s(\d+\b)\s([A-Za-z]+)+', line):
        line = re.sub(r'(?<!^)(\w+|\d+)([A-Z].*)+\s(\w+|\d+)([A-Z].*)+,\s([A-Z]{2})\s(\d+\b)\s([A-Za-z]+)+',
                      r'\1 \2 \3\n\4\n\5\n\6', line)
    line = line.split(' ')
    logging.debug('regex line: %s' % line)
    return line


url = pyperclip.paste()

logging.debug('The url is %s' % url)

# Download web page
print('Requesting download...')
res = requests.get(url)
res.raise_for_status()
print('Downloading...')

# Write contents to a file
file = open('contents.html', 'wb')
for chunk in res.iter_content(100000):
    file.write(chunk)
file.close()

fileSoup = bs4.BeautifulSoup(open('contents.html', encoding="utf-8"), features="lxml")

elems = fileSoup.select('.contact div')
logging.info('Type of elements: %s' % type(elems))
logging.info('Number of elements: %d' % len(elems))
logging.info('Type of element: %s' % type(elems[0]))
logging.info('Attributes of element: %s' % elems[0].attrs)

contentsList = []
wholeName = []
name = fileSoup.select('h1')
for n in name:
    wholeName.append(n.getText())
name = ' '.join(wholeName)
for elem in elems:
    line = re.findall('\S{1,}', elem.getText())
    if "Edit" in line:
        line.remove("Edit")
    line = get_regex_line(line)
    if "Phone" in line:
        line.remove("Phone")
    if "number" in line:
        line.remove("number")
    if "Get" in line or "to" in line or "the" in line or "website" in line:
        continue
    contentsList.append(' '.join(line))
    logging.debug('line: %s' % line)
contentsList.insert(0, name)
logging.debug('contentsList: %s' % contentsList)
contentsStr = '\n'.join(contentsList)

contents = open('contents.txt', 'w', encoding='utf-8')
contents.write(contentsStr)
contents.close()

dataFile = open('contents.txt', encoding='utf-8')
data = dataFile.readlines()
dataFile.close
for i in data:
    logging.debug('Line %d: %s' % (data.index(i) + 1, i))
