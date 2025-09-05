import sys

input = sys.stdin.readline

while True:
    line = input()
    if not line:
        break
    s, t = line.strip().split()

    i = 0
    j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    if i == len(s):
        print("Yes")
    else:
        print("No")