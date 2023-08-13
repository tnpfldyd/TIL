from collections import deque
import sys, bisect
input = sys.stdin.readline

N, T = map(int, input().split())
points = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x : x[1])

q = deque([(0, 0, 0)])
visited = set()
visited.add((0, 0))
while q:
    x, y, cnt = q.popleft()
    if y == T:
        print(cnt)
        break

    cur = bisect.bisect_left(points, y - 2, key=lambda x : x[1])
    

    for i in range(cur, N):
        nx, ny = points[i]
        if abs(ny - y) > 2:
            break
        if (nx, ny) not in visited and abs(nx - x) <= 2:
            visited.add((nx, ny))
            q.append((nx, ny, cnt + 1))
else:
    print(-1)