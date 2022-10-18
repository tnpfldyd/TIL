from collections import deque
import sys
INF = sys.maxsize
input = sys.stdin.readline
N, M = int(input()), int(input())
floyd = [[INF] * N for _ in range(N)]
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    floyd[a][b] = 1; floyd[b][a] = 1
    matrix[a].append(b); matrix[b].append(a)
for i in range(N):
    floyd[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            floyd[i][j] = min(floyd[i][j], floyd[i][k]+floyd[k][j])
for i in range(N):
    for j in range(N):
        if floyd[i][j] == INF:
            floyd[i][j] = 0
visited = [False] * N
result = []
for i in range(N):
    if not visited[i]:
        visited[i] = True
        start = deque()
        arr = []
        temp1, temp2 = INF, 0
        start.append(i)
        arr.append(i)
        while start:
            x = start.popleft()
            for k in matrix[x]:
                if not visited[k]:
                    visited[k] = True
                    start.append(k)
                    arr.append(k)
        for j in arr:
            if max(floyd[j]) < temp1:
                temp1 = max(floyd[j])
                temp2= j
        result.append(temp2+1)
print(len(result))
result.sort()
for i in result:
    print(i)