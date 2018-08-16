
'''
Problem Statement:-

Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

Input Format

There are  lines of numeric input:
The first line has a double,  (the cost of the meal before tax and tip).
The second line has an integer,  (the percentage of  being added as tip).
The third line has an integer,  (the percentage of  being added as tax).
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_amount = float(tip_percent * meal_cost / 100)
    tax_amount = float(tax_percent * meal_cost / 100)
    total = meal_cost + tip_amount + tax_amount
    if(total-int(total)>0.5):
        total = int(total)+1
    else:
        total = int(total)
    return total

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    cost = solve(meal_cost, tip_percent, tax_percent)

    print("The total meal cost is %d dollars."%(cost))
