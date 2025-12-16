import re, sys
input = sys.stdin.readline

T = int(input().strip())
pattern = re.compile(r'^[A-F]?A+F+C+[A-F]?$')

for _ in range(T):
    s = input().strip()
    if pattern.match(s):
        print("Infected!")
    else:
        print("Good")