import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
springs = list(map(int, input().split()))
visited = set(springs)
queue = []
for spring in springs:
    heapq.heappush(queue, (1, spring - 1))
    heapq.heappush(queue, (1, spring + 1))

total_unhappiness = 0
houses_built = 0

while houses_built < K:
    dist, pos = heapq.heappop(queue)
    if pos in visited:
        continue
    visited.add(pos)
    total_unhappiness += dist
    houses_built += 1
    heapq.heappush(queue, (dist + 1, pos - 1))
    heapq.heappush(queue, (dist + 1, pos + 1))

print(total_unhappiness)