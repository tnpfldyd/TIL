import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

S.sort()

can_make = 0

for num in S:
    if num > can_make + 1:
        break
    can_make += num

print(can_make + 1)