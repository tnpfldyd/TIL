import heapq, sys
input = sys.stdin.readline
 
max_heap = []
min_heap = []
 
n = int(input())
for _ in range(n):
    val = int(input())

    if not max_heap:
        heapq.heappush(max_heap, -val)
 
    elif len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -val)
 
    else:
        heapq.heappush(min_heap, val)

    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        a = -heapq.heappop(max_heap)
        b = heapq.heappop(min_heap)
 
        heapq.heappush(max_heap, -b)
        heapq.heappush(min_heap, a)
 
    print(-max_heap[0])