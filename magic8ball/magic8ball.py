#!/usr/bin/env python3
#! python3
import random, sys

def shake_ball():
    messages = ["It is certain",
                "It is decidedly so",
                "Yes definitely",
                "Reply hazy try again",
                "Ask again later",
                "Concentrate and ask again",
                "My reply is no",
                "Outlook not so good",
                "Very doubtful"]
    
    print(messages[random.randint(0,len(messages)-1)])
        
while True:
  input("Ask a yes or no question then press ENTER to shake the ball.")
  shake_ball()
  print("Do you want to roll again? Enter 'y' or 'n'")
  tryAgain = input()
  if tryAgain.casefold() == 'y':
      continue
  elif tryAgain.casefold() == 'n':
      input("Type ENTER to exit...")
      sys.exit()
  else:
      print("Please enter 'y' or 'n'")
