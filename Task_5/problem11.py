# problem: Text Wrap
# Task:
# Given a string S and width W, wrap the string so that
# each line contains exactly W characters
# Input:
# First line: string S
# second line : integers W (width)
# output: 
# Wrapped text with width W per line
# HackerRank link: https://www.hackerrank.com/challenges/text-wrap/problem
# solution:
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
