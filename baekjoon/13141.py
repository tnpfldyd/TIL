import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())

floyd = [[INF] * N for _ in range(N)]
edges = []
for i in range(N):
    floyd[i][i] = 0
for _ in range(M):
    s, e, t = map(int, input().split())
    s -= 1; e -= 1
    if floyd[s][e] > t:
        floyd[s][e] = t
        floyd[e][s] = t
    edges.append((s, e, t))
for k in range(N):
    for i in range(N):
        for j in range(N):
            nx = floyd[i][k] + floyd[k][j]
            if floyd[i][j] > nx:
                floyd[i][j] = nx
answer = INF
for i in range(N):
    temp = 0
    for j in range(M):
        nx = floyd[i][edges[j][0]] + floyd[i][edges[j][1]] + edges[j][2]
        if temp < nx:
            temp = nx
    if answer > temp:
        answer = temp
print(answer/2)