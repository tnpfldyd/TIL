from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
A, B, C = map(int, input().split())
A -= 1; B -= 1; C -= 1
matrix = [[] for _ in range(N)]
M = int(input())
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
max_cnt = [0, 0]
def heap(i):
    start = []
    visited = [INF] * N
    visited[i] = 0
    heappush(start, [0, i])
    while start:
        x, node = heappop(start)
        if x > visited[node]:
            continue
        for k, v in matrix[node]:
            nx = x + k
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, [nx, v])
    return visited
a = heap(A); b = heap(B); c = heap(C)
for i in range(N):
    new_cnt = min(a[i], b[i], c[i])
    if new_cnt > max_cnt[0]:
        max_cnt[0] = new_cnt; max_cnt[1] = i
print(max_cnt[1] + 1)
