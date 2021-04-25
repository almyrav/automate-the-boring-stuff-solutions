#!/usr/bin/env python3
with open('/home/user/Desktop/28-05-2020.txt') as file:
    lis = [x.replace('\n', '').split(': ') for x in file]

# normal text file
for x in zip(*lis):
    for y in x:
        print(y+'\t', end='')
    print('')

input('Press ENTER to exit')
