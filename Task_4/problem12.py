## problem: Introduction to sets - Average of distinct heights
## Task:
## Given N plant heights, compute the average of distinct heights.
## formula: Average = sum of distinct heights / number of distinct heights
## Input: First line integer N, second line N  space-separted integers
## Output: Float average rounded to 3 decimal places
## HackerRank link:https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
## solution:
def average(array):
    distinct_heights = set(array)
    return sum(distinct_heights)/len(distinct_heights)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

