# problem: List comprehensions
# Task: Generate all possible coordinates [ i,j,k] for given dimensions
# excluding those where i+j+k = n
# Input:
# - Four integers x,y,z,n (each on separate line)
# output
# - List of coordinates in lexicographics order
# HackerRank link: https://www.hackerrank.com/challenges/list-comprehensions/problem
# solution:
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = [[i,j,k]
            for i in range(x+1)
            for j in range(y+1)
            for k in range(z+1)
            if i+j+k!=n]
    print(result)
