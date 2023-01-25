from collections import deque
S, E = map(int, input().split())

visited = [-1] * 100001
visited[S] = 0

start = deque()
start.append((S, [S]))

if S > E:
    print(S-E)
    for i in range(S, E-1, -1):
        print(i, end = ' ')
else:
    while start:
        x, load = start.popleft()
        if x == E:
            print(visited[x])
            print(*load)
            break
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i < 100001 and visited[i] == -1:
                visited[i] = visited[x] + 1
                start.append((i, load + [i]))