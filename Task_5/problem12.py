# problem: Split CamelCase Names
# Task:
# Given a string S (like "chrisAlan") ,split it into properly names
# Input: one line string S
# output: String with spaces before each uppercase letter(except the first)
# HackerRank link: https://www.hackerrank.com/challenges/capitalize/problem
# solution:
import math
import os
import random
import re
import sys
def solve(s):
    return " ".join([word.capitalize() for word in s.split(" ")])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

