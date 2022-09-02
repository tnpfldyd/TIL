from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
visited = [0] * (T+1)
result = [[] for _ in range(T+1)]
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    result[a].append(b)
    result[b].append(a)
start = deque()
start.append(1)
visited[1] = 1
while start:
    x = start.popleft()
    for i in result[x]:
        if visited[i] == 0:
            visited[i] = visited[x] + 1
            start.append(i)
cnt = 0
for i in visited:
    if i == 2 or i == 3:
        cnt += 1
print(cnt)