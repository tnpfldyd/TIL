import sys
input = sys.stdin.readline

n = int(input())
best = 0

for _ in range(n):
    s = list(map(int, input().split()))
    total = max(s[:2]) + sum(sorted(s[2:])[-2:])
    best = max(best, total)

print(best)