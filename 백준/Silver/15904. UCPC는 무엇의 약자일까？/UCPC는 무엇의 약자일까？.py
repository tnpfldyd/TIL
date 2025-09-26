import sys
input = sys.stdin.readline

s = input().strip()
target = "UCPC"

i = 0
for char in s:
    if i < len(target) and char == target[i]:
        i += 1

if i == len(target):
    print("I love UCPC")
else:
    print("I hate UCPC")