from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())

s_pq = []
for _ in range(N):
    heappush(s_pq, tuple(map(int, input().split())))

e_pq = []
s, e = heappop(s_pq)
heappush(e_pq, e)

while s_pq:
    s, e = heappop(s_pq)
    heappush(e_pq, e)
    if e_pq[0] <= s:
        heappop(e_pq)

print(len(e_pq))