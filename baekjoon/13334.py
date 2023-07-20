from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
edges = []
for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    edges.append((a, b))
edges = sorted(edges, key=lambda x : x[1])

target = int(input())

pq = []
result = 0

for l, r in edges:
    if r - l <= target:
        heappush(pq, l)
    else:
        continue
    while pq:
        temp = pq[0]
        if r - temp <= target:
            break
        else:
            heappop(pq)
    result = max(result, len(pq))

print(result)