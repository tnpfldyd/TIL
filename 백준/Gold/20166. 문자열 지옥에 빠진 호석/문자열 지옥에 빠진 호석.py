from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
check = defaultdict(int)
map = [list(input().strip()) for _ in range(N)]

dx, dy = [0, 0, 1, -1, 1, 1, -1, -1], [1, -1, 0, 0, 1, -1, 1, -1]

def cal(x, c):
    if x == c:
        return 0
    elif x == -1:
        return c - 1
    return x

def bfs(a, b, s):
    q = deque()
    q.append((a, b, s))

    while q:
        x, y, string = q.popleft()
        check[string] += 1
        if len(string) == 5:
            continue

        for i in range(8):
            nx, ny = cal(x + dx[i], N), cal(y + dy[i], M)
            q.append((nx, ny, string + map[nx][ny]))
            
for i in range(N):
    for j in range(M):
        bfs(i, j, map[i][j])

for _ in range(K):
    print(check[input().strip()])