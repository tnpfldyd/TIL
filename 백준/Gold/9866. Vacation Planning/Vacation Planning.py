from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M, K, Q = map(int, input().split())
matrix = [[] for _ in range(N + 1)]
rev_matrix = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    matrix[a].append((t, b))
    rev_matrix[b].append((t, a))
hub = []
for _ in range(K):
    hub.append(int(input()))
visited = [[[INF] * (N+1) for _ in range(2)] for _ in range(K)]
def heap(x, board, num, pyosik):
    start = []
    heappush(start, (0, x))
    visited[num][pyosik][x] = 0
    while start:
        cost, node = heappop(start)
        if cost > visited[num][pyosik][node]:
            continue
        for k, v in board[node]:
            nx = cost + k
            if visited[num][pyosik][v] > nx:
                visited[num][pyosik][v] = nx
                heappush(start, (nx, v))
for i in range(K):
    heap(hub[i], matrix, i, 0); heap(hub[i], rev_matrix, i, 1)
result, cnt = 0, 0
for i in range(Q):
    a, b = map(int, input().split())
    temp = INF
    for j in range(K):
        temp = min(temp, visited[j][1][a]+visited[j][0][b])
    if temp != INF:
        result += temp
        cnt += 1
print(cnt)
print(result)