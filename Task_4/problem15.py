## problem: Word Order
## Task:
## Given N words, output:
## 1. The number of distinct words
## 2. The number of occurrences for each distinct word in order of appearance
## Input: First line integer N, followed by N  lines of words
## Output: First line distinct word count,  second line occurrences
## HackerRank link: https://www.hackerrank.com/challenges/word-order/problem
## solution:
if __name__ == "__main__":
    n = int(input().strip())
    word_count = {}
    
    for _ in range(n):
        word = input().strip()
        word_count[word] = word_count.get(word,0) + 1
    print(len(word_count))
    print(" ".join(map(str, word_count.values())))
  
