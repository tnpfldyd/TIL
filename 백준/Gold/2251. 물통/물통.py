from collections import deque
a, b, c = map(int, input().split())

q = deque([(0, 0)])
visited = [[False] * (b + 1) for _ in range(a + 1)]
visited[0][0] = True
answer = []

def try_pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))
while q:
    x, y = q.popleft()
    z = c - (x + y)
    if not x:
        answer.append(z)
    water = min(x, b - y)
    try_pour(x - water, y + water)
    water = min(x, c - z)
    try_pour(x - water, y)
    water = min(y, a - x)
    try_pour(x + water, y - water)
    water = min(y, c - z)
    try_pour(x, y - water)
    water = min(z, a - x)
    try_pour(x + water, y)
    water = min(z, b - y)
    try_pour(x, y + water)

print(*sorted(answer))