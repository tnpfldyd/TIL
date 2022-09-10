from collections import deque
import sys, bisect
input = sys.stdin.readline
N, M = map(int, input().split())
result = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    result[a-1].append(b-1)
    result[b-1].append(a-1)
start = deque()
start.append(0)
visited = [-1] * N
visited[0] = 0
while start:
    x = start.popleft()
    for i in result[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            start.append(i)
print(visited.index(max(visited)) + 1, max(visited), visited.count(max(visited)))