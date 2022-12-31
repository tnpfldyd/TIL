from collections import deque
a, b, c, d = map(int, input().split())
visited = {}
start = deque()
start.append((0, 0))
visited[(0, 0)] = 0
while start:
    x, y = start.popleft()
    if x == c and y == d:
        print(visited[(x, y)])
        break
    for nx, ny in ((a,y), (x, b), (0, y), (x, 0)):
        if (nx, ny) not in visited:
            visited[(nx, ny)] = visited[(x, y)] + 1
            start.append((nx, ny))
    if x <= b - y:
        if (0, x+y) not in visited:
            visited[(0, x+y)] = visited[(x, y)] + 1
            start.append((0, x+y))
    else:
        if (x-(b-y), b) not in visited:
            visited[(x-(b-y), b)] = visited[(x, y)] + 1
            start.append((x-(b-y), b))
    if y <= a - x:
        if (x+y, 0) not in visited:
            visited[(x+y, 0)] = visited[(x, y)] + 1
            start.append((x+y, 0))
    else:
        if (a, y-(a-x)) not in visited:
            visited[(a, y-(a-x))] = visited[(x, y)] + 1
            start.append((a, y-(a-x)))
else:
    print(-1)