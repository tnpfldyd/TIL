from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())

pq = []

for _ in range(N):
    a, b = map(int, input().split())
    heappush(pq, (a, b))

pq2 = []

while pq:
    a, b = heappop(pq)
    if len(pq2) < a:
        heappush(pq2, b)
    else:
        if b > pq2[0]:
            heappop(pq2)
            heappush(pq2, b)

answer = 0

for i in pq2:
    answer += i

print(answer)