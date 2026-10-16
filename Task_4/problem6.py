## problem:Find the Runner-Up score:
## Task:
## Given n scores, store them in a list and print the runner-up score
## input: First line integer n, second line array of n integers
## output: Runner-Up score (second higjest unique value)
## HacketRank:https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
## solution:
n = int(input())
arr = map(int, input().split())
unique_scores = sorted(set(arr))
print(unique_scores[-2])
