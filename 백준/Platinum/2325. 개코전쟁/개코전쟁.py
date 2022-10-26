from heapq import heappush, heappop
from collections import deque
import sys
INF = sys.maxsize
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for i in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b, i))
    matrix[b].append((t, a, i))
def heap(num):
    start = []
    visited = [INF] * N
    visited[0] = 0
    heappush(start, [0, 0])
    while start:
        x, node = heappop(start)
        if x > visited[node]:
            continue
        for k, v, l in matrix[node]:
            if l == num:
                continue
            nx = x + k
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, [nx, v])
    return visited
visited = heap(-1)
start = deque()
temp = set()
start.append(N-1)
while start:
    x = start.popleft()
    if x == 0:
        continue
    for k, v, l in matrix[x]:
        if visited[v] + k == visited[x]:
            start.append(v)
            temp.add(l)
max_num = visited[N-1]
for i in temp:
    result = heap(i)
    if result[N-1] > max_num:
        max_num = result[N-1]
print(max_num)