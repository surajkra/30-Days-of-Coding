'''
Problem Statement
Given an array, 'A', of 'N' integers, print A's elements in reverse order as a
single line of space-separated numbers.

Input Format

The first line contains an integer, 'N' (the size of our array). 
The second line contains  space-separated integers describing array 's elements.

Print the elements of array  in reverse order as a single line of space-separated
numbers.

'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    #print(len(arr))
    for i in range(0,len(arr)):
        print(arr[len(arr)-1-i], end='')
        print(' ', end='')
