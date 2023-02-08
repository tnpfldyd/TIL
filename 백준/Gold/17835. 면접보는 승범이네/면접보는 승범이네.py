from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, K = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[b].append((t, a)) # 모든 집에서 면접장으로 오는 거리를 구하는 것보다 간선을 뒤집어서 면접지를 출발지로 두고 각 집의 거리를 구하는게 빠름.
k_list = list(map(int, input().rstrip().split())) # 면접장의 위치
start = []
visited = [INF] * N
for i in k_list:
    i -= 1
    visited[i] = 0
    heappush(start, (0, i)) # 모든 출발지의 사람들이 가장 가까운 면접장으로 가고, 다 한꺼번에 넣고 돌려도, dijkstra가 알아서 각 면접장에서 가장 가까운 집을 구해주게 됨.
while start:
    x, node = heappop(start)
    if x > visited[node]:
        continue
    for k, v in matrix[node]:
        nx = x + k
        if visited[v] > nx:
            visited[v] = nx
            heappush(start, (nx, v))
num = 0 # 가장 먼 집의 번호
result = 0 # 가장 먼 집의 거리
for i in range(N):
    if visited[i] > result:
        result = visited[i]
        num = i+1
print(num)
print(result)