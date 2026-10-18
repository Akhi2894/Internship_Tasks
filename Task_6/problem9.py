# problem: What's Your Name?
# Task:
# complete the function print_full_name(first,last) that prints
# "Hello first last! You just delved into python."
# Input: First line string (first name), second line string (last name)
# Output: Greeting message with full name
# HackerRank link: https://www.hackerrank.com/challenges/whats-your-name/problem
# solution: 
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")
    

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
