from collections import deque
import sys
input = sys.stdin.readline
T, M = map(int, input().split())
matrix = [[] for _ in range(T+1)]
for i in range(T-1):
    a, b, t = map(int, input().split())
    matrix[a].append([b, t])
    matrix[b].append([a, t])
for i in range(M):
    st, en = map(int, input().split())
    start = deque()
    start.append((st, 0))
    visited = [0] * (T+1)
    visited[st] = '0'
    while start:
        x, t = start.popleft()
        for k in matrix[x]:
            if not visited[k[0]]:
                nt = t + k[1]
                visited[k[0]] = nt
                start.append((k[0], nt))
    print(visited[en])