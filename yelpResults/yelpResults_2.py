#!/usr/bin/env python3
#! python3
# yelpResults.py - Opens several Yelp search results in the browser.

import webbrowser, requests, bs4, sys, logging
#logging.disable()
logging.basicConfig(handlers=[logging.FileHandler('yelpResultsLog.txt', 'w', 'utf-8')], level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

if len(sys.argv) > 1:
    # Get search term from command line
    search = ' '.join(sys.argv[1:])
else:
    # Ask for search term
    search = input('What are you looking for?\n')

# Get location
location = input('Where do you want to search? Enter location.\n')

# Get starting point
position = input('Which post do you want to start with? Enter a number.\n')

print('Fetching results...') # display text while downloading Yelp page
res = requests.get('https://www.yelp.com/search?find_desc=' + search + '&find_loc=' + location + '&ns=1&sortby=recommended&start=' + position)
res.raise_for_status()
logging.debug('res: %s' %res)

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features="lxml")
logging.debug('soup: %s' %soup)

# Open a browser tab for each result.
linkElems = soup.select('p > a')
logging.debug('Number of elements %d' %len(linkElems))

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://yelp.com' + linkElems[i].get('href'))
    logging.debug('linkElem is %s' %linkElems[i])
