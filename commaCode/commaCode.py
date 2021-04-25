#!/usr/bin/env python3
#! python3

import sys

def list_separator(theList):
    strList =' '.join(theList)
    print('Your list: ' + strList)
    fList = []
    for fIndex in range(0,len(theList)-1):
        fList.append(theList[fIndex])
    fListStr = ', '.join(fList)
    wholeStr = fListStr + ", and " + theList[-1]
    return wholeStr
        
        

##animalList = ['dog', 'cat', 'horse', 'turtle']
##print(list_separator(animalList))
##foodList = ['spaghetti', 'meatballs', 'chicken', 'fish', 'pho']
##print(list_separator(foodList))

#Ask user for a list
yourList = []
while True:
    print("Would you like to add an item to your list? Enter 'y' or 'n'")
    addItem = input()
    if addItem.casefold() == "y":
        newItem = input("Your item: ")
        yourList.append(newItem)
    elif addItem.casefold() == "n":
        if not yourList:
            print("List is empty")
        else:
            print("Your organized list: " + list_separator(yourList))
        print("Would you like to create a new list? Enter 'y' or 'n'")
        while True:
            newList = input()
            if newList == "y":  
                yourList = []
            elif newList == "n":
                input("Press ENTER to exit...")
                sys.exit()
            else:
                print("Please enter 'y' or 'n'")
            break
    else:
        print("Enter 'y' or 'n'")
    
