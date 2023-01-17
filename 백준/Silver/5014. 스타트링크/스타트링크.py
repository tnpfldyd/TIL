from collections import deque
F, S, G, U, D = map(int, input().split())

visited = [-1] * (F + 1)
start = deque()
start.append(S)
visited[S] = 0

while start:
    node = start.popleft()
    if node == G:
        print(visited[node])
        break
    for i in (U, -D):
        next_node = node + i
        if 0 < next_node <= F and visited[next_node] == -1:
            visited[next_node] = visited[node] + 1
            start.append(next_node)
else:
    print("use the stairs")