#!/usr/bin/env python3
#! python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def findWidths(listArray):
    # find longest string in each of inner lists
    # store max width of each column as list of integers
    colWidths = [0] * len(listArray) # creates a list containing the same number of 0 values as the number of inner lists in tableData
    # colWidths[0] can store the width of the longest string in tableData[0], colWidths[1] can store the width of the longest string in tableData[1], and so on
    #find the largest value in the colWidths list to find out what integer width to pass to the rjust() string method
   
    for i in range (0,len(colWidths)):
      index = 0
      for x in range (0,len(listArray[i])):  
        nameLength = len(listArray[i][index])
        #print("nameLength1: " + str(nameLength))
        #print("len(listArray[i][x]): " + str(len(listArray[i][x])))
        if(len(listArray[i][x])>=nameLength):
          index = x
          nameLength = len(listArray[i][x])
          #print("nameLength2: " + str(nameLength))
          colWidths[i] = nameLength 
      #print(colWidths[i])
    #print(colWidths)
    return colWidths

def printTable(listArray):
  colWidths = findWidths(listArray)
  for m in range(len(listArray[0])):
    for n in range(len(listArray)):
      print (str(listArray[n][m]).rjust(colWidths[n]),end=" ")
      n+=1
      if(n==len(listArray)):
        print("\n")
    m+=1

printTable(tableData)
    
input("\nPress enter to exit...")
