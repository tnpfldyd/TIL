from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
rooms = sorted(tuple(map(int, input().split())) for _ in range(N))

pq = []
heappush(pq, rooms[0][1])

answer = 1
for i in range(1, N):
    s, e = rooms[i]
    while pq and pq[0] <= s:
        heappop(pq)
    heappush(pq, e)
    answer = max(answer, len(pq))
print(answer)