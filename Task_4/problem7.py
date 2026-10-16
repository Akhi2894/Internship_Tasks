## problem: Split and join
## Task:
## Given a string, split it on spaces and join with hyphens
## Input: Single string line with space-separated words
## ouput: String with words joined by "-"
## HackerRank link:https://www.hackerrank.com/challenges/python-string-split-and-join/problem
## solution:
def split_and_join(line):
    return "-".join(line.split(" "))
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
