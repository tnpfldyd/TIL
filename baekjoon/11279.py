import sys
import heapq
input = sys.stdin.readline
T = int(input())
arr = []
heapq.heapify(arr)
for i in range(T):
    alpha = int(input())
    if alpha == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr, (-alpha, alpha))