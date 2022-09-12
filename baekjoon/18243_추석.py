from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
visited = [-1] * N
for i in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append(b)
    matrix[b].append(a)
result = 0
for i in range(N):
    visited = [-1] * N
    visited[i] = 0
    start = deque()
    start.append(i)
    while start:
        x = start.popleft()
        for k in matrix[x]:
            if visited[k] == -1:
                visited[k] = visited[x] + 1
                start.append(k)
    if -1 in visited or max(visited) > 6:
        result += 1
print('Big World!' if result != 0 else 'Small World!')
