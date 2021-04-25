#!/usr/bin/env python3
#! python3
import random, sys

def guess_number():
    while True:
        secretNum = random.randint(1,20)
        print("I am thinking of a number between 1 and 20.")
        #print(secretNum)
        for guess in range(1,7):
            print("Take a guess")
            try:
                yourNum = int(input())
                if yourNum < secretNum:
                    print("Your guess is too low.")
                elif yourNum > secretNum:
                    print("Your guess is too high.")
                else:
                    break #answer is correct
            except ValueError:
                print("Enter a valid number")
        if yourNum == secretNum:
            print("Congratulations! You guessed the number in " + str(guess) + " guesses.")
        else:
            print("The number I was thinking of was " + str(secretNum) + ".")
        print("Would you like to try again? Enter 'y' or 'n'")
        while True:
            tryAgain = input()
            if tryAgain.casefold() == "y":
                break
            elif tryAgain.casefold() == "n": 
                print("Goodbye")
                input("Press ENTER to exit...")
                sys.exit()
            else:
                print("Please enter 'y' or 'n'")
guess_number()

        





        
    

