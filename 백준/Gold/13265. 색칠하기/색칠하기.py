from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, color, n):
    queue = deque()
    for i in range(1, n + 1):
        if color[i] == -1:
            queue.append(i)
            color[i] = 0
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        return "impossible"
    return "possible"

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    color = [-1] * (n + 1)
    result = bfs(graph, color, n)
    print(result)