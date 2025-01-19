from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
points = list(map(int, input().split()))

q = deque([(0, 0)])
result = points[0]
visited = [False] * N
visited[0] = True
while q:
    x, cnt = q.popleft()
    if cnt >= K:
        break
    for n in matrix[x]:
        if not visited[n]:
            visited[n] = True
            result += points[n]
            q.append((n, cnt + 1))
print(result)