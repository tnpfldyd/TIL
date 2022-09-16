from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
s, e = map(int, input().split())
s -= 1; e -= 1
def heap(i):
    start = []
    visited = [INF] * N
    visited[i] = 0
    heappush(start, [0, i])
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
S = heap(s)
E = heap(e)
result = INF
V = int(input())
V_list = list(map(int, input().rstrip().split()))
for i in range(V):
    new = V_list[i] - 1
    cnt = S[new] + E[new]
    if result > cnt:
        result = cnt
print(result if result != INF else -1)