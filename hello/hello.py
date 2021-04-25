#!/usr/bin/env python3
#! python3
print('Hello world!')
while True:
    print("What's your name?") #this is how you write a comment, capiche?
    myName = input()
    print("It's good to meet you, " + myName + "!")
    print('What year is it?')
    currentYear = input()
    print('What year were you born?')
    birthYear = input()
    print('In Korea, you are ' + str(int(currentYear)-int(birthYear)+1) + ' years old.')

    print("Would you like to try again? Enter 'y' or 'n'")

    tryAgain = input()
    if tryAgain.casefold() == "y":
        continue
    elif tryAgain.casefold() == "n": 
        print("Goodbye")
        input("Press ENTER to exit...")
        sys.exit()
    else:
        print("Please enter 'y' or 'n'")
