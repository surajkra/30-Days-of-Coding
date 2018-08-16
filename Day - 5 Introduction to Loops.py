'''
Problem Statement:
Given an integer, 'n' , print its first 'i' multiples. Each multiple  (where ) should
be printed on a new line in the form: n x i = result.

'''

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    for i in range(1,11):
        print("%d x %d = %d"%(n,i,n*i))
