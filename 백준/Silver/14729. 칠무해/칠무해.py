import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    score = float(input())
    if len(heap) < 7:
        heapq.heappush(heap, -score)
    else:
        if -heap[0] > score:
            heapq.heappop(heap)
            heapq.heappush(heap, -score)

result = sorted([-x for x in heap])

for score in result:
    print(f"{score:.3f}")