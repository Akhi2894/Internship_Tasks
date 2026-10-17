## problem: Find substring occurrences
## Task:
## Givem a string and a substring, count how many times the substring occurs in the string
## Input:
## First line: original string
## second line : substring
## ouput:
## Integers count of occurrences
## HackerRank link: https://www.hackerrank.com/challenges/find-a-string/problem
## solution:
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)- len(sub_string)+1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
