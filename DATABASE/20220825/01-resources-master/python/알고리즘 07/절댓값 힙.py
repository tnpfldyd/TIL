"""
-1
1
0
-1
-1
1
1
-2
2
0
"""
from heapq import *
N = 18
heap = []
X = [1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0]

# heappop 값을 뺄 때
root = heappop(heap)
print(root[1])

# heappush 값을 넣을 때
heappush(heap,[abs(x),x])
