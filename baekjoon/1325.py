from collections import deque; import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    matrix[b].append(a)
result = []
max_cnt = 0
for i in range(1, N+1):
    start = deque()
    start.append(i)
    visit = [0]*(N+1)
    cnt = 0
    visit[i] = 1
    while start:
        x = start.popleft()
        for j in matrix[x]:
            if visit[j] == 0:
                visit[j] = 1
                start.append(j)
                cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
    result.append((i, cnt))
for i in result:
    if i[1] == max_cnt:
        print(i[0], end = ' ')
