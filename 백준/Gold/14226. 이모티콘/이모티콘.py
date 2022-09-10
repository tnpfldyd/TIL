from collections import deque
T = int(input())
start = deque()
visited = [[-1] * (T+1) for _ in range(T+1)]
start.append((1, 0))
visited[1][0] = 0
while start:
    x, clip = start.popleft()
    if x == T:
        print(visited[x][clip])
        break
    for i in range(3):
        if i == 0 and visited[x][x] == -1:
            visited[x][x] = visited[x][clip] + 1
            start.append((x, x))
        elif i == 1 and x+clip <= T and visited[x+clip][clip] == -1:
            visited[x+clip][clip] = visited[x][clip] + 1
            start.append((x+clip, clip))
        else:
            if 0 <= x-1 and visited[x-1][clip] == -1:
                visited[x-1][clip] = visited[x][clip] + 1
                start.append((x-1, clip))