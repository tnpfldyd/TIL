from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
godola = {}
A, B, K, G = map(int, input().split())
gload = list(map(int, input().strip().split()))
matrix = [[] for _ in range(N+1)]
temp = [{} for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    matrix[a].append((t, b))
    matrix[b].append((t, a))
    temp[a][b] = t
    temp[b][a] = t
time = 0
for i in range(G-1):
    a, b = gload[i], gload[i+1]
    t = temp[a][b]
    godola[(a, b)] = (time, time+t)
    godola[(b, a)] = (time, time+t)
    time += t
start = []
heappush(start, [K, A])
visited = [INF] * (N+1)
visited[A] = K
while start:
    cnt, node = heappop(start)
    if cnt > visited[node]:
        continue
    for k, v in matrix[node]:
        temp = godola.get((node, v))
        if temp and temp[0] <= cnt <= temp[1]:
            nx = temp[1] + k
        else:
            nx = cnt + k
        if visited[v] > nx:
            visited[v] = nx
            heappush(start, [nx, v])
print(visited[B]-K)