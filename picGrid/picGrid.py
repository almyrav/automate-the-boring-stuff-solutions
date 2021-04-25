#!/usr/bin/env python3
#! python3
import sys
heart = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
    

def draw_pic(pic):
    for elements in range(0,len(pic[0])):
        print('\n')
        for index in range(0,len(pic)):
            print(pic[index][elements], end=' ')
            
print("Would you like to draw a picture? Enter 'y' or 'n'")
drawPic = input()
if drawPic == "y":
    draw_pic(heart)
    input("\n Press ENTER to exit...")
elif drawPic == "n":
    input("Press ENTER to exit...")
    
    
