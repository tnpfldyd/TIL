import sys

N, K = map(int, sys.stdin.readline().split())
diamonds = [int(sys.stdin.readline()) for _ in range(N)]

diamonds.sort()

max_count = 0
l = 0

for r in range(N):
    while diamonds[r] - diamonds[l] > K:
        l += 1
    max_count = max(max_count, r - l + 1)

print(max_count)