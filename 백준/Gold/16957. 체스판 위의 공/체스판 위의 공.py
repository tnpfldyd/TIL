def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

r, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
parent = [0] * (r * c)
ans = [0] * (r * c)

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(r):
    for j in range(c):
        y, x = i, j
        for k in range(8):
            ny, nx = i + dy[k], j + dx[k]
            if not (0 <= ny < r and 0 <= nx < c):
                continue
            if a[y][x] > a[ny][nx]:
                y, x = ny, nx
        parent[i * c + j] = y * c + x

for i in range(r):
    for j in range(c):
        ans[find(i * c + j)] += 1

for i in range(r):
    print(" ".join(map(str, ans[i * c:(i + 1) * c])))