import sys, heapq
input = sys.stdin.readline

N = int(input())

pq = []
for _ in range(N):
    a, b = map(int, input().split())
    heapq.heappush(pq, (a, b))

pq2 = []

while pq:
    a, b = heapq.heappop(pq)
    if len(pq2) < a:
        heapq.heappush(pq2, b)
    else:
        if b > pq2[0]:
            heapq.heappop(pq2)
            heapq.heappush(pq2, b)

answer = 0

while pq2:
    answer += heapq.heappop(pq2)

print(answer)