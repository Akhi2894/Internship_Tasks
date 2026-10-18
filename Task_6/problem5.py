# problem : Leap Year
# Task: Determine if a given year is a leap year in the gregorian calendar
# Input:
# - A single integer y (year)
#  constraints:
# -1900 <= y <= 10^5
# output:
# - return True if leap year, else False
# HackerRank link: https://www.hackerrank.com/challenges/write-a-function/problem
# solution:
def is_leap(year):
    if  year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


year = int(input())
print(is_leap(year))
