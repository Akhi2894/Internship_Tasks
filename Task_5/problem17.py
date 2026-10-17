## problem: Happiness score
## Task:
## Given an array of integers and two  sets A and B:
## - if element belongs to A = add +1 to happiness
## - if element belongs to B = add -1 to happines
## -else = no change
## Input:
## First line: n(array size), m(set size)
## second line: array of n integers
## third line: set A (m integers)
## fourth line : set B (m integers)
## output:
## final happiness score (integer)
## HackerRank link: https://www.hackerrank.com/challenges/no-idea/problem
## solutions:
if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int,input().split()))
    A = set(map(int, input().split()))
    B = set(map(int,input().split()))
    
    
    happiness = 0
    for num in arr:
        if num in A:
            happiness += 1
        elif num in B:
            happiness -= 1
    print(happiness)
