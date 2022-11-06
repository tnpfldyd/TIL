from collections import deque
import sys
input = sys.stdin.readline
N, H, M = map(int, input().split())
matrix = [[] for _ in range(N)]
hyper = [[] for _ in range(M)]
for i in range(M):
    num = list(map(int, input().strip().split()))
    for j in num:
        matrix[j-1].append(i)
        hyper[i].append(j-1)
visited_matirx = [False] * N
visited_hyper = [False] * M
start = deque()
start.append((0, 1))
visited_matirx[0] = True
while start:
    x, cnt = start.popleft()
    if x == N-1:
        print(cnt)
        break
    temp = []
    for i in matrix[x]:
        if not visited_hyper[i]:
            visited_hyper[i] = True
            temp.append(i)
    for i in temp:
        for j in hyper[i]:
            if not visited_matirx[j]:
                visited_matirx[j] = True
                start.append((j, cnt+1))
else:
    print(-1)