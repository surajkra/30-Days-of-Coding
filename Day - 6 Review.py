'''
Task
Given a string, 'S', of length 'N'  that is indexed from '0' to 'N-1' , print
its even-indexed and odd-indexed characters as '2' space-separated strings on a
single line

Note:  is considered to be an even index.

Input Format

The first line contains an integer, 'N' (the number of test cases).
Each line  of the  subsequent lines contain a String, .

Sample Input
2
Hacker
Rank

Sample Output
Hce akr
Rn ak
'''
N = input()
str = []

for i in range(0,int(N)):
    str = input()
    out = []
    for j in range(0,len(str)):
        if(j % 2 == 0):
            out.append(str[j])
    out.append(' ')
    for k in range(0,len(str)):
        if(k % 2 != 0):
            out.append(str[k])
    out = ''.join(out)
    print(out)
