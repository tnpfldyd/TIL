import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == '0':
        break
    print('yes' if s == s[::-1] else 'no')