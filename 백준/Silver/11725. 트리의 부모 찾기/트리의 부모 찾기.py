from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
ew = [[] for _ in range(T+1)]
visit = [0] * (T+1)
for i in range(T-1):
    a, b = map(int, input().split())
    ew[a].append(b)
    ew[b].append(a)
start = deque()
start.append(1)
visit[1] = 1
while start:
    x = start.popleft()
    for i in ew[x]:
        if visit[i] == 0:
            visit[i] = x
            start.append(i)
for i in range(2, len(visit)):
    print(visit[i])