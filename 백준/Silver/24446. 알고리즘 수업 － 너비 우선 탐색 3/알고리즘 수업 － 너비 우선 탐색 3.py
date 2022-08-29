from collections import deque
import sys
input = sys.stdin.readline
N, M, R = map(int, input().split())
result = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    result[a].append(b)
    result[b].append(a)
for i in range(N+1):
    result[i].sort(reverse=True)
start = deque()
start.append(R)

visited[R] = '0'
while start:
    x = start.popleft()
    for i in result[x]:
        if visited[i] == 0:
            start.append(i)
            visited[i] = int(visited[x]) + 1
for i in visited[1:]:
    if i == 0:
        print(-1)
    else:
        print(i)