from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())

times = []
pq = []

for _ in range(N):
    _, s, e = map(int, input().split())
    heappush(times, (s, e))
    
result = 0

while times:
    s, e = heappop(times)
    while pq and pq[0] <= s:
        heappop(pq)
    
    heappush(pq, e)
    result = max(result, len(pq))

print(result)