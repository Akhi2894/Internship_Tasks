## problem: Average marks
## Task:
## Given N students with their marks, store them in a dictionary and print the average marks.
## Average should be printed correct to 2 decimal places
## Input: First line integer N, followed by N lines with "name marks"
## output: Float average marks rounded to 2 decimal places
## HackerRank link: https://www.hackerrank.com/challenges/finding-the-percentage/problem
## solution
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0],list(map(float,line[1:]))
        student_marks[name] = scores

    query_name = input()
    avg = sum(student_marks[query_name])/len(student_marks[query_name])
    print(f"{avg:.2f}")
