'''
Problem Statement
Given 'n' names and phone numbers, assemble a phone book that maps friends' names
to their respective phone numbers. You will then be given an unknown number of
names to query your phone book for. For each 'name' queried, print the associated
entry from your phone book on a new line in the form name=phoneNumber;
if an entry for  is not found, print 'Not found' instead.

'''

N = input()
phonebook = {}
for i in range(0,int(N)):
    str1,str2 = input().split()
    phonebook[str1] = str2

for i in range(0,int(N)):
    str = input()
    if(str in phonebook):
        print(str,end='')
        print("=",end='')
        print(phonebook[str])
    else:
        print("Not found")
