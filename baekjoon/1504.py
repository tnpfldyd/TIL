from heapq import heappop,heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
n1, n2 = map(int, input().split())
n1 -= 1; n2 -= 1
def dijkstra(s):
    start = []
    heappush(start, (0, s))
    visited = [INF] * N
    visited[s] = 0
    while start:
        x, node = heappop(start)
        if x > visited[node]:
            continue
        for k, v in matrix[node]:
            nx = x + k
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, (nx, v))
    return visited
# 다익스트라 안에서 2개의 정점을 거쳐서 N-1로 가는 길은 다익스트라 안에서 구현하려면 구현이 힘들 수 있음.
# 차라리 출발지를 3군데로 놓고 다익스트라를 돌린 뒤,
# 0 > 첫번째 노드 > 두번째 노드 > 도착지 or 0 > 두번째 노드 > 첫번째 노드 > 도착지의 두 가지 경로중 싼 비용을 출력하는게 낫다 생각함.
zero_start = dijkstra(0) # 0으로 출발하는 다익스트라
n1_start = dijkstra(n1) # n1 정점으로 출발하는 다익스트라
n2_start = dijkstra(n2) # n2 정점으로 출발하는 다익스트라
# 3가지 기준으로 출발을 한 뒤에, 
# 0 > n1 정점 > n2 정점 > N-1 에 도착하는 경로와,
# 0 > n2 정점 > n1 정점 > N-1 에 도착하는 경로를 비교하여 둘 중에 작은 값을 출력 하면 됨.
answer = min(zero_start[n1] + n1_start[n2] + n2_start[N-1], zero_start[n2] + n2_start[n1] + n1_start[N-1]) 
# zero_start[n1] 은 0 > n1의 거리를 표현, n1_start[n2] 은 n1 > n2 거리를 표현, n2_start[N-1] 은 n2 > 도착지의 거리를 뜻함
print(answer if answer < INF else -1)