## problem: Print Function
## Task: 
## Given an integer n, print the sequence 123...n without spaces
## input: Single integer n
## ouput: Print numbers from 1 to n as a continuous string
## HackerRank link:https://www.hackerrank.com/challenges/python-print/problem
## solution:
n = int(input())
for i in range(1,n+1):
  print(i, end="")
