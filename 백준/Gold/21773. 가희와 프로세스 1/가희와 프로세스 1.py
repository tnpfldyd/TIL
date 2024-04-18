from heapq import heappop, heappush
import sys
input = sys.stdin.readline

T, N = map(int, input().split())
pq = []
for _ in range(N):
    a, b, c = map(int, input().split())
    heappush(pq, (-c, a, b))

for _ in range(T):
    if not pq:
        break
    value, name, time = heappop(pq)
    print(name)
    time -= 1
    if time:
        heappush(pq, (value + 1, name, time))