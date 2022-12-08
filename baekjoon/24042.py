from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((i, b))
    matrix[b].append((i, a))
visited = [INF] * N
visited[0] = 0
start = []
heappush(start, [0, 0])
while start:
    cost, node = heappop(start)
    if cost > visited[node]:
        continue
    for k, v in matrix[node]:
        nx = cost + (k - cost) % M + 1
        # 음수의 %
        # 파이썬에서는 -1 % 10 > -1 + 10 % 10 으로 작동함 (C언어에서는 다르게 작동함)
        # k 신호등 불 켜지는 시간 - 현재 cost % 총 신호등 갯수 + 이동시간 1
        # 신호등 갯수가 12개고 
        # 현재 건너려는 신호등주기가 0, 12, 24, 36 분일때 
        # 현재 코스트가 10이면 0 - 10 % 12 = 2 가 나오고 2분 뒤에 신호등이 켜진다는 뜻
        # nx = 10 + 2분뒤 + 이동거리 1 로 13이 됨.
        if visited[v] > nx:
            visited[v] = nx
            heappush(start, [nx, v])
print(visited[N-1])
