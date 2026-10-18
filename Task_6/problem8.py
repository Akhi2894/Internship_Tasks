# problem: Tuples
# Task: Create a tuple from given integers and print  its hash value
# Input:
# - First line: integer n (number of elements)
# - second line: n space-seprated integers
# output:
# -print(hash(t))
# HackerRank link: https://www.hackerrank.com/challenges/python-tuples/problem

# Note: HackerRank's expected output (3713081631934410656) was generated with
# Python 3.7 or older. Python 3.8+ changed the tuple hashing algorithm, so
# hash((1, 2)) now returns -3550055125485641917. The logic below is correct.

# solution:
f __name__ == "__main__":
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
# The sample test case fails on HackerRank because its expected output was generated with Python 3.7 or earlier.
# Since Python 3.8, tuple hashing uses a different algorithm (xxHash-based), so hash((1, 2)) returns -3550055125485641917 on current Python 3 and PyPy 3.
# The solution is correct. Only the platform's expected value is outdated

