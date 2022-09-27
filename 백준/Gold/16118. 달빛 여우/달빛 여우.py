from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for i in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
def fox(s):
    start = []
    heappush(start, [0, s])
    visited = [INF] * N
    visited[0] = 0
    while start:
        x, node = heappop(start)
        if x > visited[node]:
            continue
        for k, v in matrix[node]:
            nx = k + x
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, [nx, v])
    return visited
def wolf(s):
    start = []
    visited2 = [[INF] * N for _ in range(2)]
    visited2[0][0] = 0
    heappush(start, [0, s, 0])
    while start:
        x, node, cur = heappop(start)
        if x > visited2[cur][node]:
            continue
        if cur == 0:
            for k, v in matrix[node]:
                nx = k/2 + x
                if visited2[1][v] > nx:
                    visited2[1][v] = nx
                    heappush(start, [nx, v, cur+1])
        else:
            for k, v in matrix[node]:
                nx = k*2 + x
                if visited2[0][v] > nx:
                    visited2[0][v] = nx
                    heappush(start, [nx, v, cur-1])
    return visited2
foxy = fox(0)
wolfy = wolf(0)
cnt = 0
for i in range(N):
    if wolfy[0][i] > wolfy[1][i]:
        if wolfy[1][i] > foxy[i]:
            cnt += 1
    else:
        if wolfy[0][i] > foxy[i]:
            cnt += 1
print(cnt)