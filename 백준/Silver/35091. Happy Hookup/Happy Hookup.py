from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

boy, girl = map(int, input().split())

def get_reachable(start):
    reachable = [False] * (N + 1)
    q = deque([start])
    reachable[start] = True

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not reachable[nxt]:
                reachable[nxt] = True
                q.append(nxt)

    return reachable

boy_reachable = get_reachable(boy)

visited = [False] * (N + 1)
q = deque([girl])
visited[girl] = True

while q:
    cur = q.popleft()
    if boy_reachable[cur]:
        print("yes")
        print(cur)
        break
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)
else:
    print("no")