## problem: set - distinct country stamps
## Task:
## Given N country names, count the total number of distinct country stamps
## Input: First line integer N, followed by N lines of country names
## Output: Integer count of distinct country names
## HackerRank link: https://www.hackerrank.com/challenges/py-set-add/problem
## solution:
if __name__ == "__main__":
    n = int(input().strip())
    countries = set()
    for _ in range(n):
        countries.add(input().strip())
    print(len(countries))

