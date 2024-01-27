from collections import deque
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

matrix = [[] for _ in range(5001)]

def input_graph():
    for _ in range(N - 1):
        p, q, r = map(int, input().split())
        matrix[p].append((r, q))
        matrix[q].append((r, p))

def bfs(k, v):
    cnt = 0
    visited = [False] * 5001
    visited[v] = True

    q = deque([v])

    while q:
        now = q.popleft()

        for next_road, next_node in matrix[now]:
            if visited[next_node] or next_road < k:
                continue

            cnt += 1
            visited[next_node] = True
            q.append(next_node)

    return cnt

def solve():
    for _ in range(Q):
        k, v = map(int, input().split())
        print(bfs(k, v))

input_graph()
solve()
