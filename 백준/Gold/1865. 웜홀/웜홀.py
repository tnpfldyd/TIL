import sys
input = sys.stdin.readline
INF = sys.maxsize
T = int(input())
for _ in range(T):
    N, M, H = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b, t = map(int, input().split())
        a -= 1; b -= 1
        edges.append((a, b, t))
        edges.append((b, a, t))
    for _ in range(H):
        a, b, t = map(int, input().split())
        a -= 1; b -= 1
        edges.append((a, b, -t))
    answer = False
    visited = [INF] * N
    visited[0] = 0
    for i in range(N):
        for edge in edges:
            cur = edge[0]
            next_node = edge[1]
            cost = edge[2]
            if visited[next_node] > visited[cur] + cost:
                visited[next_node] = visited[cur] + cost
                if i == N - 1:
                    answer = True
    print('YES' if answer else 'NO')