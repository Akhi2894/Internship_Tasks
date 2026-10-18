# problem: Designer Door Mat
# Task: Print a door Mat design with given dimensions
# Input:
# - single line: N M (space-separated)
# constarints:
# -1<=N<=101
# -M = 3*N
# output:
# Door mat pattern
# HackerRank link: https://www.hackerrank.com/challenges/designer-door-mat/problem
# solution:

if __name__ == "__main__":
    N,M = map(int, input().split())
    
    for i in range(1,N,2):
        pattern = (".|."*i).center(M,"-")
        print(pattern)
    print("WELCOME".center(M,"-"))
    for i in range(N-2,0,-2):
        pattern = (".|."*i).center(M,"-")
        print(pattern)
