#!/usr/bin/env python3
#! python3
# copyYelp.py - Open browser tab with yelp results from a single page

import webbrowser, requests, bs4, sys, pyperclip, logging
logging.disable()
#logging.basicConfig(filename='copyYelpLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Get web page from clipboard
address = pyperclip.paste()
logging.debug('The web page is %s' %address)

print('Fetching results...') # display text while downloading Yelp page
res = requests.get(address)
res.raise_for_status()
logging.debug('res: %s' %res)

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features="lxml")
logging.debug('soup: %s' %soup)

# Open a browser tab for each result.
linkElems = soup.select('p > a')
logging.debug('Number of elements %d' %len(linkElems))

numOpen = min(10, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://yelp.com' + linkElems[i].get('href'))
    logging.debug('linkElem is %s' %linkElems[i])
