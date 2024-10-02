import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N, K = map(int, input().split())
colors = list(map(int, input().split()))
max_heap = []

for i, count in enumerate(colors):
    heappush(max_heap, [-count, i])

is_valid = True
result = []
temp = []

while max_heap:
    count, color_index = heappop(max_heap)
    result.append(color_index + 1)
    
    if len(result) >= 2 and result[-1] == result[-2]:
        is_valid = False
        break

    if temp:
        previous = temp.pop()
        if previous[0] < 0:
            heappush(max_heap, previous)    

    temp.append([count + 1, color_index])

if not is_valid or temp[0][0] <= -1:
    print(-1)
else:
    print(*result)