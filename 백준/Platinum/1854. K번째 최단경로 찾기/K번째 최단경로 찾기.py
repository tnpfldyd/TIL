from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, K = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
visited = [[INF] * K for _ in range(N)]
visited[0][0] = 0
start = []
heappush(start, [0, 0])
while start:
    x, node = heappop(start)
    for k, v in matrix[node]:
        nx = x + k
        if visited[v][K-1] > nx:
            visited[v][K-1] = nx
            visited[v].sort() # K번째의 visited를 바꾼 다음, 오름차순으로 정렬하여 K번째가 구해질때까지 계속 다익스트라를 도는 방식.
            heappush(start, [nx, v])
for i in range(N):
    print(visited[i][K-1] if visited[i][K-1] != INF else -1)