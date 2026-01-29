import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split())

teleport = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    teleport[x].append(y)
    teleport[y].append(x)

dist = [-1] * (N + 1)
q = deque([S])
dist[S] = 0

while q:
    cur = q.popleft()

    if cur == E:
        print(dist[cur])
        break

    if cur > 1 and dist[cur - 1] == -1:
        dist[cur - 1] = dist[cur] + 1
        q.append(cur - 1)

    if cur < N and dist[cur + 1] == -1:
        dist[cur + 1] = dist[cur] + 1
        q.append(cur + 1)

    for nxt in teleport[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)