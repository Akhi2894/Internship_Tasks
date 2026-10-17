## problem: Symmetric Difference
## Task:
## Given two sets of integers A and B, print their symmetric difference in  ascending order
## symmetric difference = value in A or B  but not in both
## Input:
## First line integer N, second line N space-separated integers (setA)
## Third line integer M, fourth line M space-separated integers (set B)
## output:
## symmetric difference integers in ascending order, one per line
## HackerRank link:https://www.hackerrank.com/challenges/symmetric-difference/problem
## solution:
if __name__ == "__main__":
    n = int(input().strip())
    a = set(map(int, input().split()))
    m = int(input().strip())
    b = set(map(int, input().split()))
    
    result = sorted(a.symmetric_difference(b))
    for val in result:
        print(val)
