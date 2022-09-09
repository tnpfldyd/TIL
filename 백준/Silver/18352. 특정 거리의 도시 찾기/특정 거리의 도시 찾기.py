from collections import deque
import sys
input = sys.stdin.readline
N, M, K, S = map(int, input().split())
matrix = [[] for _ in range(N+1)]
start = deque()
start.append(S)
visited = [-1] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
visited[S] = 0
answer = False
result = []
while start:
    x = start.popleft()
    if visited[x] == K:
        result.append(x)
        answer = True
    for i in matrix[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            start.append(i)
result.sort()
for i in result:
    print(i)
if not answer:
    print(-1)