import sys
input = sys.stdin.readline

S = input().strip()

def is_palindrome(s):
    return s == s[::-1]

for i in range(len(S)):
    extended = S + S[:i][::-1]
    if is_palindrome(extended):
        print(len(extended))
        break