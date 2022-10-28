from collections import deque
import sys
input = sys.stdin.readline
N, M, S = map(int, input().split())
S -= 1
matrix = [[] for _ in range(N)]
rev_matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append(b)
    rev_matrix[b].append(a)
start = deque()
start.append(S)
visited = [False] * N
visited[S] = True
cnt = 0
while start:
    x = start.popleft()
    for k in matrix[x]:
        if not visited[k]:
            visited[k] = True
            cnt += 1
            start.append(k)
cnt2 = 0
visited = [False] * N
visited[S] = True
start.append(S)
while start:
    x = start.popleft()
    for k in rev_matrix[x]:
        if not visited[k]:
            visited[k] = True
            cnt2 += 1
            start.append(k)
print(cnt2+1, N-cnt)