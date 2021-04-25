#!/usr/bin/env python3
#! python3

def printMenu(title, itemsDict, leftWidth, rightWidth):
    print(title.upper().center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwhiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printMenu('picnic items', picnicItems, 12, 5)
printMenu('picnic items', picnicItems, 20, 6)

input("Press enter to exit...")
