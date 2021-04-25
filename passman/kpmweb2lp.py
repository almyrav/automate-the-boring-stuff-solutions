#!/usr/bin/env python3
#kpmweb2lp.py -- converts website passwords from kaspersky password manager txt export to lastpass csv
import csv, os
def get_list(listHeading):
    with open(os.path.abspath(os.path.dirname(__file__)) + os.sep + 'kpmpasswords.txt') as file:
        lis = [x.replace('---', '').split('\n') for x in file]
        
    listName = []
    # normal text file
    for x in lis:

        if 'Applications' in x: # ignore application passwords
            break
        
        info = [y.split(': ') for y in x]
        if info[0][0] == listHeading:
            listName.append(info[0][1])
    return listName


url = get_list('Website URL')
username = get_list('Login')
password = get_list('Password')
extra = get_list('Comment')
name = get_list('Website name')
grouping = []
fav = []

with open(os.path.abspath(os.path.dirname(__file__)) + os.sep + 'import2LastPass.csv', mode='w') as csv_file:
    fieldnames = ['url', 'username', 'password','extra','name','grouping','fav']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(password)):
        writer.writerow({fieldnames[0]: url[i], fieldnames[1]: username[i], fieldnames[2]: password[i],fieldnames[3]: extra[i],fieldnames[4]: name[i],fieldnames[5]: '',fieldnames[6]: 0})

    print('CSV file saved to ' + os.path.abspath(os.path.dirname(__file__)) + os.sep + 'import2LastPass.csv')
input('Press ENTER to exit')
