# 8 11 1 0 5
# 0 1 10
# 0 2 10
# 1 2 10
# 2 6 40
# 6 7 10
# 5 6 10
# 3 5 15
# 3 6 40
# 3 4 20
# 1 4 20
# 1 3 20
# 4 7

from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, A, S, E = map(int, input().split())
matrix = [[] for _ in range(N)]
air = {}
for _ in range(M):
    a, b, t = map(int, input().split())
    matrix[a].append((t, b))
    matrix[b].append((t, a))
for _ in range(A):
    a, b = map(int, input().split())
    if a not in air:
        air[a] = [b]
    else:
        air[a].append(b)
start = []
heappush(start, [0, 0, S])
visited = [INF] * N
visited[S] = 0
while start:
    x, cnt, node = heappop(start)
    if x > visited[node] and cnt:
        continue
    for k, v in matrix[node]:
        nx = x + k
        if visited[v] > nx:
            visited[v] = nx
            heappush(start, [nx, cnt, v])
    if not cnt and air.get(node):
        for k in air[node]:
            if visited[k] > x:
                visited[k] = x
                heappush(start, [x, cnt+1, k])
print(visited[E])


from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, A, S, E = map(int, input().split())
matrix = [[] for _ in range(N)]
air = {}
for _ in range(M):
    a, b, t = map(int, input().split())
    matrix[a].append((t, b))
    matrix[b].append((t, a))
def heap(S):
    start = []
    heappush(start, [0, S])
    visited = [INF] * N
    visited[S] = 0
    while start:
        x, node = heappop(start)
        if x > visited[node]:
            continue
        for k, v in matrix[node]:
            nx = x + k
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, [nx, v])
    return visited
answer = heap(S)[E]
for _ in range(A):
    a, b = map(int, input().split())
    answer = min(answer, heap(S)[a] + heap(b)[E])
print(answer)