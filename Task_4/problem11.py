## problem: String validation
## Task:
## Given a string s, check and print:
## 1. True if any character is alphanumeric
## 2. True if any character is alphabetic
## 3. True if any character is a digit
## 4. True if any character is lowercase
## 5. True if any character is uppercase
## Input: Single string s
## Output: Five lines with True/False
## HackerRank link:https://www.hackerrank.com/challenges/string-validators/problem
## Solution:
if __name__ == '__main__':
    s = input().strip()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
