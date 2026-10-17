# Problem: The Minion Game
# Task:
# Determine the winner of the game and print their name with score.
# If scores are equal, print "Draw".
# Input:
# - A single line string S (uppercase letters only).
# - Constraints: 0 < |S| ≤ 10^5
# Output:
# - Print "Kevin <score>" or "Stuart <score>" depending on winner.
# - If scores are equal, print "Draw".
# HackerRank link: https://www.hackerrank.com/challenges/the-minion-game/problem
# solution:

def minion_game(string):
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i
    if kevin_score > stuart_score:
        print("kevin, kevin_score")
    elif stuart_score > kevin_score:
        print("stuart", stuart_score)
    else:
        print("Draw")
