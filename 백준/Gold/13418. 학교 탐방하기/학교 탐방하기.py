from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N+1)]
matrix2 = [[] for _ in range(N+1)]
for _ in range(M+1):
    a, b ,t = map(int, input().split())
    t = 0 if t == 1 else 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
    matrix2[a].append((-t, b))
    matrix2[b].append((-t, a))
visited = [False] * (N+1)
visited2 = [False] * (N+1)
result, cnt = 0, 0
result2, cnt2 = 0, 0
start = []
start2 = []
heappush(start, [0, 0])
heappush(start2, [0, 0])
while start:
    x, node = heappop(start)
    if cnt == N+1:
        break
    if not visited[node]:
        visited[node] = True
        cnt += 1
        result += x
        for k, v in matrix[node]:
            if not visited[v]:
                heappush(start, [k, v])
while start2:
    x, node = heappop(start2)
    if cnt2 == N+1:
        break
    if not visited2[node]:
        visited2[node] = True
        cnt2 += 1
        result2 += x
        for k, v in matrix2[node]:
            if not visited2[v]:
                heappush(start2, [k, v])
print(result2 ** 2 - result ** 2)