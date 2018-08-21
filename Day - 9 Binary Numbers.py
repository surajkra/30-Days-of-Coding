'''

Given a base-10 integer,'n' , convert it to binary (base-). Then find and print
the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
'''


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    max_count = 0
    flag = 0
    flag_count = 0
    dec_num = n
    while(dec_num > 0):
        rem = dec_num % 2
        dec_num = int(dec_num / 2)
        if(rem == 1):
            flag_count=flag_count+1
        else:
            flag_count = 0
        if(max_count < flag_count):
            max_count = flag_count

    print(max_count)
