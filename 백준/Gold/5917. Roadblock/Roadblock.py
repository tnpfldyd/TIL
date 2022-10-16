from heapq import heappop, heappush
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
def heap(w):
    visited = [INF] * N
    visited[0] = 0
    start = []
    heappush(start, [0, 0])
    while start:
        x, node = heappop(start)
        if x > visited[node]:
            continue
        for k, v, l in matrix[node]:
            if l == w:
                nx = x + (k*2)
            else:
                nx = x + k
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, [nx, v])
    return visited
one = heap(-1)
temp = set()
restart = deque()
restart.append(N-1)
while restart:
    x = restart.popleft()
    for k, v, l in matrix[x]:
        if one[x] == one[v] + k and l not in temp:
            temp.add(l)
            restart.append(v)
result = 0
for i in temp:
    final = heap(i)
    nload = final[N-1] - one[N-1]
    if nload > result:
        result = nload
print(result)