from collections import deque
import sys
input = sys.stdin.readline

N, S, E = map(int, input().split())
matrix = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    x, y, cost = map(int, input().split())
    matrix[x].append((y, cost))
    matrix[y].append((x, cost))

visited = [False] * (N + 1)
q = deque()
q.append((S, 0, 0))
visited[S] = True

while q:
    cur_node, total_cost, max_cost = q.popleft()
    if cur_node == E:
        print(total_cost - max_cost)
        break

    for nxt_node, nxt_cost in matrix[cur_node]:
        if not visited[nxt_node]:
            visited[nxt_node] = True
            q.append((nxt_node, total_cost + nxt_cost, max(max_cost, nxt_cost)))