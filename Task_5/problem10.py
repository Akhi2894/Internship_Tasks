# problem: Swap Case
# Task:
# Given a string s, convert all lowercase letter to uppercase
# and all uppercase letters to lowercase
#Input:one line string s
# Output: Modified string with swapped cases
# HackerRank link: https://www.hackerrank.com/challenges/swap-case/problem
# solution:
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
