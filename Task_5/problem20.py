# HackerRank Problem: Piling Up!
# Task:
# Determine if cubes can be stacked by picking from left or right.
# Input Format:
# - First line: integer T (number of test cases)
# - For each test case:
#   - Line 1: integer n (number of cubes)
#   - Line 2: n space-separated integers (cube side lengths)
# Output Format:
# - For each test case, print "Yes" or "No"
# HackerRank link: https://www.hackerrank.com/challenges/piling-up/problem
# solution:
from collections import deque
def piling_up(cubes):
    d = deque(cubes)
    top = float('inf')
    while d:
        if d[0] >= d[-1]:
             pick = d.popleft()
        else:
            pick = d.pop()
        if pick > top:
            return "No"
        top = pick
    return "Yes"

if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        cubes = list(map(int, input().split()))
        print(piling_up(cubes))
