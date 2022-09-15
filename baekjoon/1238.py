from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, s = map(int, input().split())
matrix = [[] for _ in range(N)]

for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
cnt = 0
def code(s):
    start = []
    heappush(start, [0, s-1])
    visited = [INF] * N
    visited[s-1] = 0
    while start:
        x, node = heappop(start)
        if x > visited[node]:
            continue
        for nt, k in matrix[node]:
            nx = nt + x
            if visited[k] > nx:
                visited[k] = nx
                heappush(start, [nx, k])
    return visited
visit = code(s)
for i in range(1, N+1):
    if i == s:
        continue
    result = code(i)
    dkdh = result[s-1] + visit[i-1]
    if dkdh > cnt:
        cnt = dkdh
print(cnt)
