# HackerRank Problem: Merge the Tools!
# Task:
# Given a string s and integer k, split s into n/k substrings of length k.
# For each substring, remove duplicate characters while preserving order.
# Print each processed substring on a new line.
# Input:
# - First line: string s
# - Second line: integer k
# Output:
# - Print each processed substring on a new line
# HackerRank link: https://www.hackerrank.com/challenges/merge-the-tools/problem
# solution:
def merge_the_tools(s,k):
    for i in range(0,len(s), k):
        substring = s[i:i+k]
        seen = set()
        result = []
        for ch in substring:
            if ch not in seen:
                seen.add(ch)
                result.append(ch)
        print("".join(result))
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
