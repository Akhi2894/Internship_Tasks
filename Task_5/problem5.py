# Problem: String Validators
# Task:
# Given a string S, check if it contains:
# 1. Alphanumeric characters
# 2. Alphabetical characters
# 3. Digits
# 4. Lowercase characters
# 5. Uppercase characters
# Input: One line string S
# Output: 5 lines of True/False for each condition
# HackerRank link: https://www.hackerrank.com/challenges/string-validators/problem
# solution:
if __name__ == '__main__':
    s = input().strip()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

