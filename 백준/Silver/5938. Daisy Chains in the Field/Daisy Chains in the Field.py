from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
visited = [False] * (N + 1)
q = deque([1])
visited[1] = True
while q:
    x = q.popleft()
    for n in matrix[x]:
        if not visited[n]:
            visited[n] = True
            q.append(n)
cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        print(i)
        cnt += 1
if not cnt:
    print(0)