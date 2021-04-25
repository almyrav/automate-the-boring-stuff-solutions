#!/usr/bin/env python3
#! python3
# lucky.py - Opens several Google search results.

import webbrowser, requests, bs4, sys, pyperclip, logging
logging.basicConfig(handlers=[logging.FileHandler('luckyLog.txt', 'w', 'utf-8')], level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

if len(sys.argv) > 1:
    # Get address from command line
    search = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    search = pyperclip.paste()


print('Googling...') # display text while downloading the Google page
res = requests.get('https://google.com/search?q=' + search)
res.raise_for_status()
logging.debug('res: %s' %res)

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features="lxml")
logging.debug('soup: %s' %soup)

# Open a browser tab for each result.
linkElems = soup.select('span a')
logging.debug('Number of elements %d' %len(linkElems))

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
    logging.debug('linkElem is %s' %linkElems[i])
