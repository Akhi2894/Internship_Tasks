## problem: Mutations
## Task:
## Strings are immutable in python. Given a string and an index with a character
## replace the character at that undex with the new one and return the modified string
## Input: String s, integer i, character c
## Output: Modified string with s[i] replaced by c
HackerRank link:https://www.hackerrank.com/challenges/python-mutations/problem
## solution:
def mutate_string(string, position, character):
    s_list = list(string)
    s_list[position] = character
    return "".join(s_list)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
