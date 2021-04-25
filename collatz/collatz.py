#!/usr/bin/env python3
#! python3
import sys

def collatz(number):
    if number % 2 == 0:
        print(str(number) + " divided by 2 is " + str(number//2))
        return number // 2
    else:
        print("(" + str(number) + "x3)+1=" + str(3 * number + 1))
        return 3 * number + 1

while True:
    print("Enter number")
    try:
        yourNum = int(input())
        while yourNum != 1:
            yourNum = collatz(yourNum)
            print(yourNum)
        print("Do you want to try again? Enter 'y' or 'n'")
        while True:
            tryAgain = input()
            if tryAgain.casefold() == 'y':
                break
            elif tryAgain.casefold() == 'n':
                input("Press ENTER to exit...")
                sys.exit()
            else:
                print("Please enter 'y' or 'n'")
    except ValueError:
        print("You must enter an integer.")
    
