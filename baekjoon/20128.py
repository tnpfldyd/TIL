from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]

for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))

visited = [[INF] * 2 for _ in range(N)]
visited[0][1] = 0
start = []
heappush(start, [0, 0])
while start:
    cost, node = heappop(start)
    if cost != visited[node][0] and cost != visited[node][1]:
        continue
    for k, v in matrix[node]:
        nx = cost + k
        if nx % 2:
            if visited[v][0] > nx:
                visited[v][0] = nx
                heappush(start, [nx, v])
        else:
            if visited[v][1] > nx:
                visited[v][1] = nx
                heappush(start, [nx, v])
for i in range(N):
    answer = []
    if visited[i][0] == INF:
        answer.append(-1)
    else:
        answer.append(visited[i][0])
    if visited[i][1] == INF:
        answer.append(-1)
    else:
        answer.append(visited[i][1])
    print(*answer)