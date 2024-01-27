from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
pq = []
total = 0

for _ in range(N):
    a, b = map(int, input().split())
    heappush(pq, (a, b))
    total += b

temp = 0
mid = total / 2
while pq:
    a, b = heappop(pq)
    temp += b
    if temp >= mid:
        print(a)
        break