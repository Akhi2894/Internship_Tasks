## problem: Find substring occurrences
## Task:
## Given a string and a substring, print the number of times the substring occurs in the string
## Input: First line original string, second line substring
## Output: Integer count of occurrences
## HackerRank link:
## solution:https://www.hackerrank.com/challenges/find-a-string/problem
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
