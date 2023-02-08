from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, K = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[b].append((t, a)) # 모든 집에서 면접장으로 오는 거리를 구하는 것보다 간선을 뒤집어서 면접지를 출발지로 두고 각 집의 거리를 구하는게 빠름. K <= N 의 조건 때문에,
    # 그리고 면접장을 출발지로 잡아야, 모든 면접장에서 한꺼번에 출발해도 문제가 안생김. 기존 집을 다 0으로 만들고 다익스트라를 돌리게 되면, 도착지에 도착을 못하는 경우가 생김. 
k_list = list(map(int, input().rstrip().split())) # 면접장의 위치
start = []
visited = [INF] * N
for i in k_list:
    i -= 1 # 인풋이 0~N-1이 아니라 1 ~ N 이기 때문에 -1
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
        num = i+1 # 인풋에서 받은 값을 -1 한 것을 + 1
print(num)
print(result)