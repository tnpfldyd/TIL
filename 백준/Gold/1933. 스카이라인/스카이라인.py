import sys
import heapq
input = sys.stdin.readline

N = int(input())
events = []
for _ in range(N):
    L, H, R = map(int, input().split())
    events.append((L, -H, R))
    events.append((R, 0, 0))

events.sort()

result = []
heap = [(0, float('inf'))]
prev_height = 0

for x, negH, R in events:
    if negH != 0:
        heapq.heappush(heap, (negH, R))
    while heap[0][1] <= x:
        heapq.heappop(heap)
    curr_height = -heap[0][0]
    if curr_height != prev_height:
        result.append((x, curr_height))
        prev_height = curr_height

for x, h in result:
    print(x, h, end=' ')