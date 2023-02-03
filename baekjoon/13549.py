import sys
from heapq import heappop, heappush
INF = sys.maxsize
S, E = map(int, input().split())
visited = [INF] * 100001
start = []
heappush(start, (0, S))
visited[S] = 0
while start:
    cnt, x = heappop(start)
    if x == E:
        print(cnt)
        break
    for i in (x-1, x+1, x*2):
        if 0 <= i < 100001:
            if i == x*2:
                next_cost = cnt
            else:
                next_cost = cnt + 1
            if visited[i] > next_cost:
                visited[i] = next_cost
                heappush(start, (next_cost, i))