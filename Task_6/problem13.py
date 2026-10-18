# HackerRank Problem: Set Union
# Task:
# Find total distinct students subscribed to at least one newspaper.
# Input Format:
# - First line: integer n (English subscribers count)
# - Second line: n space-separated roll numbers
# - Third line: integer b (French subscribers count)
# - Fourth line: b space-separated roll numbers
# Output Format:
# - Print total distinct roll numbers
# HackerRank link: https://www.hackerrank.com/challenges/py-set-union/problem
# solution:
if __name__ == "__main__":
    n= int(input())
    english = set(map(int, input().split()))

    b = int(input())
    french = set(map(int, input().split()))
    union_set = english.union(french)

print(len(union_set))
