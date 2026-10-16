## problem: Python Loops
## Task:
## Given an integer n, print the square of all non-negative integers i<n.
## input: Single integer n
## output: Print i*2 for each i in range(0,n)
## HackerRank link:https://www.hackerrank.com/challenges/python-loops/problem
## solution:
n = int(input().strip())
for i in range(n):
  print(i**2)
    
