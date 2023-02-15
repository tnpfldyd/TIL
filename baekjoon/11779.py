from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
M = int(input())
visited = [INF] * N
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
s, e = map(int, input().split())
s -= 1; e -= 1
start = []
heappush(start, (0, s, [s + 1])) # cost, 시작점, list 형식의 노드 ( +1 은 편의상 모든 정점의 번호를 -1 해주었기 때문에.) 29번줄도 같은 이유다.
visited[s] = 0
while start:
    x, node, load = heappop(start)
    if x > visited[node]:
        continue
    if node == e:
        print(x)
        print(len(load))
        print(*load)
        break
    for cost, v in matrix[node]:
        nx = x + cost
        nload = load + [v + 1]
        if visited[v] > nx:
            visited[v] = nx
            heappush(start, (nx, v, nload))