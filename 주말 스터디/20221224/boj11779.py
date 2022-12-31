from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
M = int(input())
visited = [[INF, []] for _ in range(N)]
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    matrix[a-1].append((t, b-1))
s, e = map(int, input().split())
start = []
heappush(start, [0, s-1, [s]])
visited[s-1][0] = 0
while start:
    x, node, load = heappop(start)
    if x > visited[node][0]:
        continue
    for T, k in matrix[node]:
        nx = T + x
        nload = load + [k+1]
        if visited[k][0] > nx:
            visited[k][0] = nx
            visited[k][1] = nload
            heappush(start, [nx, k, nload])
print(visited[e-1][0])
print(len(visited[e-1][1]))
print(*visited[e-1][1])