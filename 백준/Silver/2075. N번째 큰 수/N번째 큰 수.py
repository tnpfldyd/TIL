import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    row = list(map(int, input().split()))
    for num in row:
        heapq.heappush(heap, num)
        if len(heap) > N:
            heapq.heappop(heap)

print(heap[0])