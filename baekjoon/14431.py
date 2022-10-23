from heapq import heappop, heappush
import sys, math
input = sys.stdin.readline
INF = sys.maxsize
sx, sy, ex, ey = map(int, input().split())
N = int(input())
nodes = [(sx, sy), (ex, ey)]
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
for _ in range(N):
    a, b = map(int, input().split())
    nodes.append((a, b))
matrix = [[] for _ in range(len(nodes))]
for i in range(len(nodes)):
    for j in range(i, len(nodes)):
        if i != j:
            ix, iy = nodes[i]; jx, jy = nodes[j]
            cost = int(((ix - jx) ** 2 + (iy - jy) ** 2) ** 0.5)
            if cost > 1:
                if is_prime_number(cost):
                    matrix[i].append((cost, j))
                    matrix[j].append((cost, i))
visited = [INF] * len(nodes)
start = []
visited[0] = 0
heappush(start, [0, 0])
while start:
    cost, now = heappop(start)
    if cost > visited[now]:
        continue
    for k, v in matrix[now]:
        nx = cost + k
        if visited[v] > nx:
            visited[v] = nx
            heappush(start, [nx, v])
print(visited[1] if visited[1] != INF else -1)