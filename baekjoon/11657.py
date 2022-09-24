import sys
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
edges = []
visited = [INF] * n
for _ in range(m):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    edges.append((a, b, t))
visited[0] = 0
answer = False
for i in range(n):
    for j in range(m):
        cur = edges[j][0]
        next_node = edges[j][1]
        cost = edges[j][2]
        if visited[cur] != INF and visited[next_node] > visited[cur] + cost:
            visited[next_node] = visited[cur] + cost
            if i == n - 1:
                answer = True
if answer:
    print(-1)
else:
    for i in range(1, n):
        if visited[i] == INF:
            print(-1)
        else:
            print(visited[i])