# Problem: Second Lowest Grade
# Task:
# Given names and grades of N students, print the names of students
# having the second lowest grade in alphabetical order.
# Input:
#   First line integer N (number of students)
#   Next 2N lines: name and grade
# Output:
#   Names of students with second lowest grade, each on new line
# HackerRank link: https://www.hackerrank.com/challenges/nested-list/problem
# solution
if __name__ == "__main__":
    n = int(input().strip())
    records = []

    for _ in range(n):
        name = input().strip()
        grade = float(input().strip())
        records.append([name, grade])

    grades = sorted(set([grade for _, grade in records]))
    second_lowest = grades[1]

    result = [name for name, grade in records if grade == second_lowest]

    for name in sorted(result):
        print(name)
