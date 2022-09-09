from collections import deque
s, e = map(int, input().split())
visited = [-1] * 100001
start = deque()
start.append((s, [s]))
visited[s] = 0
if s > e:
    print(s-e)
    for i in range(s, e-1, -1):
        print(i, end = ' ')
else:
    while start:
        x, key = start.popleft()
        if x == e:
            print(visited[x])
            print(*key)
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i < 100001 and visited[i] == -1:
                visited[i] = visited[x] + 1
                start.append((i, key+[i]))