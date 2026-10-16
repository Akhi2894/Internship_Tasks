## problem: Shoe shop earnings
## Task:
## Raghu owns a shoe shop, Given the shoe sizes available and customer customer request,
## compute the total money earned.
## Input:
## First line integer X (number os shoes)
## second line X space-separated integers (shoe size)
## Third line integers N (number of customers)
## next N lines: shoe size desired and price
## output:
## total money earned
## HackerRank link: https://www.hackerrank.com/challenges/collections-counter/problem
## solution:
from collections import Counter

if __name__ == "__main__":
    x = int(input().strip())
    sizes = list(map(int,input().split()))
    n = int(input().strip())
    
    inventory = Counter(sizes)
    earnings = 0
    
    for _ in range(n):
        size, price = map(int, input().split())
        if inventory[size] > 0:
            earnings += price
            inventory[size] -=1
    print(earnings)    
