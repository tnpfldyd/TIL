from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, C = map(int, input().split())
S, E = map(int, input().split())
S -= 1; E -= 1
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
visited = [[INF] * N for _ in range(N)]
visited[S][0] = 0
start = []
heappush(start, [0, 0, S])
while start:
    x, cnt, node = heappop(start)
    if x > visited[node][cnt]:
        continue
    for i in range(cnt):
        if visited[node][i] < x:
            break
    else:
        for k, v in matrix[node]:
            nx = x + k
            if  N > cnt + 1 and visited[v][cnt+1] > nx:
                visited[v][cnt+1] = nx
                heappush(start, [nx, cnt+1, v])
print(min(visited[E]))
for i in range(C):
    tax = int(input())
    for j in range(len(visited[E])):
        visited[E][j] += (j*tax)
    print(min(visited[E]))