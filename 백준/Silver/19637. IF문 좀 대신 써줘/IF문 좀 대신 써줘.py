import sys
import bisect
input = sys.stdin.readline

N, M = map(int, input().split())

titles = []
limits = []

for _ in range(N):
    title, limit = input().split()
    titles.append(title)
    limits.append(int(limit))

for _ in range(M):
    power = int(input())
    idx = bisect.bisect_left(limits, power)
    if idx < N and limits[idx] >= power:
        print(titles[idx])
    else:
        print(titles[N-1])