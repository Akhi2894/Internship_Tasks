## problem: Find the Runner-up score!
## Task:
## Given participate scores,print the runner-up score(second highest)
##Input:
## First line integer n (number of scores)
## second line n space-separated integers A[i]
## ouput:
Runner-up score(integer)
## HackerRank link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
## solution:
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    unique_scores = list(set(arr))
    unique_scores.sort(reverse = True)
    print(unique_scores[1])
    
    
