#!/usr/bin/env python3
#! python3

import sys

theBoard = {'top-L': ' ','top-M': ' ','top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
printBoard(theBoard)
plays = 0
while True:
    if not ((theBoard['top-L'] == 'X' and theBoard['top-M'] == 'X' and theBoard['top-R'] == 'X') or
        (theBoard['mid-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['mid-R'] == 'X') or
            (theBoard['low-L'] == 'X' and theBoard['low-M'] == 'X' and theBoard['low-R'] == 'X') or
            (theBoard['top-L'] == 'X' and theBoard['mid-L'] == 'X' and theBoard['low-L'] == 'X') or
            (theBoard['top-M'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-M'] == 'X') or
            (theBoard['top-R'] == 'X' and theBoard['mid-R'] == 'X' and theBoard['low-R'] == 'X') or
            (theBoard['top-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-R'] == 'X') or
            (theBoard['top-R'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-L'] == 'X') or
        (theBoard['top-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-L'] == 'O') or
            (theBoard['top-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-R'] == 'O') or
            (theBoard['top-R'] == 'O' and theBoard['mid-R'] == 'O' and theBoard['low-R'] == 'O') or
            (theBoard['top-M'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-M'] == 'O') or
            (theBoard['top-L'] == 'O' and theBoard['mid-L'] == 'O' and theBoard['low-L'] == 'O') or
            (theBoard['low-L'] == 'O' and theBoard['low-M'] == 'O' and theBoard['low-R'] == 'O') or
            (theBoard['mid-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['mid-R'] == 'O') or
            (theBoard['top-L'] == 'O' and theBoard['top-M'] == 'O' and theBoard['top-R'] == 'O') or
            plays > 8):
        
        print('Turn for ' + turn + '. Move on which space?')
        print('1.top-left\n2.top-center\n3.top-right\n4.mid-left\n5.mid-center\n6.mid-right\n7.low-left\n8.low-center\n9.low-right')
        move = input()
        if move == '1' and theBoard['top-L'] is ' ':
            theBoard['top-L'] = turn
        elif move == '2' and theBoard['top-M'] is ' ':
            theBoard['top-M'] = turn
        elif move == '3' and theBoard['top-R'] is ' ':
            theBoard['top-R'] = turn
        elif move == '4' and theBoard['mid-L'] is ' ':
            theBoard['mid-L'] = turn
        elif move == '5' and theBoard['mid-M'] is ' ':
            theBoard['mid-M'] = turn
        elif move == '6' and theBoard['mid-R'] is ' ':
            theBoard['mid-R'] = turn
        elif move == '7' and theBoard['low-L'] is ' ':
            theBoard['low-L'] = turn
        elif move == '8' and theBoard['low-M'] is ' ':
            theBoard['low-M'] = turn
        elif move == '9' and theBoard['low-R'] is ' ':
            theBoard['low-R'] = turn
        else:
            plays -= 1
            if turn == 'X':
                player = 'X'
                turn = 'O'
            else:
                player = 'O'
                turn = 'X'
            print("Please enter a number from 1 to 9 and select a space that isn't taken")
        printBoard(theBoard)
        if turn == 'X':
            player = 'X'
            turn = 'O'
        else:
            player = 'O'
            turn = 'X'
        plays += 1
        print("plays:" + str(plays))
    else:
        if plays == 9:
            print("It's a tie! Would you like to play again? Enter 'y' or 'n'")
            plays = 0
        else:
            print("Player " + player + " won!" + "Would you like to play again? Enter 'y' or 'n'")
            plays = 0
        while True:
            tryAgain = input()
            if tryAgain.casefold() == "y":
                theBoard = {'top-L': ' ','top-M': ' ','top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
                printBoard(theBoard)
                break
            elif tryAgain.casefold() == "n": 
                print("Goodbye")
                input("Press ENTER to exit...")
                sys.exit()
            else:
                print("Please enter 'y' or 'n'")
    
