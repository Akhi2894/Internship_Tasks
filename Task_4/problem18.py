## problem: List operations
## Task:
## perform operations on a list based on given command
## 1. insert i e
## 2. print
## 3. remove e
## 4. append e
## 5. sort
## 6. pop
## 7. reverse
## Input: First ;ine integer N, followed by N lines of commands
## Ouput: Results of "print" commands
## HackerRank link: https://www.hackerrank.com/challenges/python-lists/problem
## solution:
if __name__ == '__main__':
    N = int(input().strip())
    lst = []
    
    for _ in range(N):
        cmd = input().split()
        if cmd[0] == 'insert':
            lst.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == 'print':
            print(lst)
        elif cmd[0] == 'remove':
            lst.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            lst.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            lst.sort()
        elif cmd[0] == 'pop':
            lst.pop()
        elif cmd[0] == 'reverse':
            lst.reverse()
