from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, s = map(int, input().split()) # 정점, 간선, 파티 지점
s -= 1
matrix = [[] for _ in range(N)]
rev_matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    rev_matrix[b].append((t, a)) # 역방향으로 만들어줌. 1 > x > 2 거리가 최단 거리면 2 > x > 1 거리가 최단 거리 임을 이용
cnt = 0
def dijkstra(s, board): # 넘겨받은 2차원 배열 사용
    start = []
    heappush(start, (0, s))
    visited = [INF] * N
    visited[s] = 0
    while start:
        x, node = heappop(start)
        if x > visited[node]:
            continue
        for nt, k in board[node]:
            nx = nt + x
            if visited[k] > nx:
                visited[k] = nx
                heappush(start, (nx, k))
    return visited

visit = dijkstra(s, matrix) # 시작 정점과, 정방향 2차원 배열 넘겨줌
rev_visit = dijkstra(s, rev_matrix) # 역방향으로 시작정점과, 역방향 2차원 배열 넘겨줌
result = 0
for i in range(N):
    nx = visit[i] + rev_visit[i] # 정방향과 역방향 돈 경로 중 가장 큰 걸 정답으로 출력
    if result < nx:
        result = nx
print(result)
