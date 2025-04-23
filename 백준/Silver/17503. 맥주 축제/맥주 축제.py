import sys
import heapq

input = sys.stdin.readline
n, m, k = map(int, input().split())
beers = []

for _ in range(k):
    v, c = map(int, input().split())
    beers.append((v, c))

beers.sort(key=lambda x: x[1])

pq = []
total = 0

for v, c in beers:
    heapq.heappush(pq, v)
    total += v

    if len(pq) > n:
        total -= heapq.heappop(pq)

    if len(pq) == n and total >= m:
        print(c)
        sys.exit()

print(-1)