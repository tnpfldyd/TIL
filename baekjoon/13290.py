from heapq import heappop, heappush
from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize
water = int(input())
water_list = list(map(int, input().strip().split()))
matrix = [[] for _ in range(water)]
M = int(input())
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
start = []
visited = [INF] * water
visited[0] = 0
heappush(start, [0, 0])
while start:
    x, node = heappop(start)
    if x > visited[node]:
        continue
    for k, v in matrix[node]:
        nx = x + k
        if visited[v] > nx:
            visited[v] = nx
            heappush(start, [nx, v])
if visited[water-1] == INF:
    print('impossible')
else:
    result = 0
    restart = deque()
    restart.append((water-1, water_list[water-1]))
    while restart:
        x, cnt = restart.popleft()
        if x == 0:
            if result < cnt:
                result = cnt
        for k, v in matrix[x]:
            if visited[v] == visited[x] - k:
                restart.append((v, water_list[v]+cnt))
    print(visited[water-1], result)