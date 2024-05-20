from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
pq = []
for _ in range(N):
    heappush(pq, int(input()))

result = 0    
while len(pq) > 1:
    c = heappop(pq) + heappop(pq)
    result += c
    heappush(pq, c)
    
print(result)