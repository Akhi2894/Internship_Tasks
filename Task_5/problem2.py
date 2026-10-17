## problem : String split and join
## Task:
## Given a string , split it on spaces and join using '-'
## Input: One line string with space-seprated words
## output: String with wors joines by '-'
## HackerRank link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
## solution:
def split_and_join(line):
    return "-".join(line.split(" "))
    
if __name__ == "__main__":
    line = input().strip()
    result = split_and_join(line)
    print(result)
