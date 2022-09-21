from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
person = list(map(int, input().rstrip().split()))
visited = [0] * N
visit = [0] * N
for i in range(N):
    if person[i] == -1:
        continue
    matrix[person[i]-1].append(i)
    visit[i] = person[i]-1
for i in range(M):
    a, w = map(int, input().split())
    a -= 1
    visited[a] += w
start = deque()
start.append(0)
while start:
    x = start.popleft()
    visited[x] += visited[visit[x]]
    for k in matrix[x]:
        start.append(k)
print(*visited)
