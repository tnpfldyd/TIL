from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

pq = []
max_value = 0 

for i in range(N):
    heappush(pq, A[i])
    max_value = max(max_value, A[i])

v = pq[0]
cur_max = max_value
min_diff = max_value - v

while pq[0] <= max_value:
    v = heappop(pq)
    min_diff = min(min_diff, cur_max - v)
    heappush(pq, 2 * v)
    cur_max = max(cur_max, 2 * v)

print(min(min_diff, cur_max - pq[0]))