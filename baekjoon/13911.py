from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[] for _ in range(N+2)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
macN, maccost = map(int, input().split())
mac_list = set(map(int, input().strip().split()))
starN, starcost = map(int, input().split())
star_list = set(map(int, input().strip().split()))
for i in mac_list:
    matrix[N].append((0, i-1))
    matrix[i-1].append((0, N))
for i in star_list:
    matrix[N+1].append((0, i-1))
    matrix[i-1].append((0, N+1))
def heap(node):
    start = []
    heappush(start, [0, node])
    visited = [INF] * (N+2)
    visited[node] = 0
    while start:
        cost, cur = heappop(start)
        if cost > visited[cur]:
            continue
        for k, v in matrix[cur]:
            if v != N and v != N+1:
                nx = cost + k
                if visited[v] > nx:
                    visited[v] = nx
                    heappush(start, [nx, v])
    return visited
mac = heap(N)
star = heap(N+1)
result = INF
for i in range(N):
    if i+1 not in mac_list and i+1 not in star_list:
        m, s = mac[i], star[i]
        if m <= maccost and s <= starcost:
            if result > m + s:
                result = m + s
print(result if result != INF else -1)