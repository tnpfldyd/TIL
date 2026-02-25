import sys
input = sys.stdin.readline

L = int(input())
S = sorted(map(int, input().split()))
n = int(input())

if n in S:
    print(0)
    sys.exit()

low = 0
high = 0
for x in S:
    if x < n:
        low = x
    elif x > n:
        high = x
        break

print((n - low) * (high - n) - 1)