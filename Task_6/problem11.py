# problem: String Formatting
# Task:
# print decimal, octal, hexadecimal, and binary values for numbers 1 to n
# Input:
# - single integer n
# output:
# -Each line: decimal octal hexadecimal binary (right-aligned)
# HackeRank link: https://www.hackerrank.com/challenges/python-string-formatting/problem
# solution:

def print_formatted(number):
    width = len(bin(number)) -2   #width of binary representation
    for i in range(1, number+1):
        print(str(i).rjust(width),
             oct(i)[2:].rjust(width),
             hex(i)[2:].upper().rjust(width),
             bin(i)[2:].rjust(width))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
