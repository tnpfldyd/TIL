# from collections import deque
# import sys
# input = sys.stdin.readline
# N, K = map(int, input().rstrip().split())
# list_ = [-1] * 100001
# start = deque()
# start.append(N)
# list_[N] = 0
# while start:
#     x = start.popleft()
#     if x == K:
#         print(list_[x])
#         break
#     for i in (x*2, x-1, x+1):
#         if i == x*2:
#             if 0 <= i < 100001 and list_[i] == -1:
#                 list_[i] = list_[x]
#                 start.append(i)
#         elif 0 <= i < 100001 and list_[i] == -1:
#             list_[i] = list_[x] + 1
#             start.append(i)
from heapq import heappop, heappush
N, K = map(int, input().split())
list_ = set()
start = []
heappush(start, [0, N])
list_.add(N)
while start:
    cnt, x = heappop(start)
    if x == K:
        print(cnt)
        break
    for i in (x-1, x+1, x*2):
        if i == x*2:
            if 0 <= i < 100001 and i not in list_:
                list_.add(i)
                heappush(start, [cnt, i])
        elif 0 <= i < 100001 and i not in list_:
            list_.add(i)
            heappush(start, [cnt+1, i])