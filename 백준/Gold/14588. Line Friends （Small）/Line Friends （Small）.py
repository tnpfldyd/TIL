import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
graph = [[INF] * (N) for _ in range(N)]
lines = [tuple(map(int, input().split())) for _ in range(N)]
for i in range(N):
    graph[i][i] = 0

for i in range(N):
    for j in range(N):
        if lines[i][1] >= lines[j][0] and lines[j][1] >= lines[i][0]:
            graph[i][j] = 1
            graph[j][i] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

Q = int(input())

for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    answer = graph[a][b]
    print(answer if answer != INF else -1)