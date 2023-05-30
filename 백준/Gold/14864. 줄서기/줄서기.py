import sys
input = sys.stdin.readline
N, M = map(int, input().split())

v = [i for i in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    v[a] += 1; v[b] -= 1

visited = [False] * (N + 1)

for i in range(1, N + 1):
    if v[i] > N or v[i] <= 0:
        print(-1)
        break
    if visited[v[i]]:
        print(-1)
        break
    visited[v[i]] = True
else:
    for i in range(1, N + 1):
        print(v[i], end=' ')