from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
stations = []
for _ in range(N):
    a, b = map(int, input().split())
    stations.append((a, b))

stations.sort()
L, P = map(int, input().split())
pq = []

cnt, cur = 0, 0
ans = True

while P < L:
    while cur < N and P >= stations[cur][0]:
        heappush(pq, -stations[cur][1])
        cur += 1
    if not pq:
        ans = False
        break
    P -= heappop(pq)
    cnt += 1

print(cnt if ans else - 1)