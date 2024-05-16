from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
E = int(input())
T = int(input())
matrix = [[] for _ in range(N + 1)]
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    matrix[b].append((c, a))
    
pq = [(0, E)]
visited = [INF] * (N + 1)
visited[E] = 0
while pq:
    c, x = heappop(pq)
    if c > T:
        break
    if visited[x] < c:
        continue
    for nc, nx in matrix[x]:
        a = nc + c
        if visited[nx] > a:
            visited[nx] = a
            heappush(pq, (a, nx))

cnt = 0
for v in visited:
    if v <= T:
        cnt += 1
        
print(cnt)