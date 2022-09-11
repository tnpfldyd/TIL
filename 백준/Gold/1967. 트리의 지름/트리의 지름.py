from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
matrix = [[] for _ in range(T+1)]
for i in range(T-1):
    a, b, t = map(int, input().split())
    matrix[a].append([b, t])
    matrix[b].append([a, t])
max_cnt = 0
for i in range(1, T+1):
    start = deque()
    start.append((i, 0))
    visited = [0] * (T+1)
    visited[i] = '0'
    while start:
        x, t = start.popleft()
        for k in matrix[x]:
            if not visited[k[0]]:
                nt = t + k[1]
                visited[k[0]] = nt
                start.append((k[0], nt))
    visited[i] = 0
    if max_cnt < max(visited):
        max_cnt = max(visited)
print(max_cnt)