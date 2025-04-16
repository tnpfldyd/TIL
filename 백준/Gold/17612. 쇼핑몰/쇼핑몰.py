import heapq
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
customers = [tuple(map(int, input().split())) for _ in range(N)]

counters = [(0, i) for i in range(K)]
heapq.heapify(counters)

leaving_heap = []

for idi, wi in customers:
    wait_time, counter_id = heapq.heappop(counters)
    finish_time = wait_time + wi
    heapq.heappush(leaving_heap, (finish_time, -counter_id, idi))
    heapq.heappush(counters, (finish_time, counter_id))

result = 0
rank = 1
while leaving_heap:
    _, _, idi = heapq.heappop(leaving_heap)
    result += rank * idi
    rank += 1

print(result)