import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [input().strip() for _ in range(N)]
ans = -1

for i in range(N):
    for j in range(M):
        n = int(A[i][j])
        root = int(n ** 0.5)
        if root * root == n:
            ans = max(ans, n)
        for dx in range(-N + 1, N):
            for dy in range(-M + 1, M):
                if dx == 0 and dy == 0:
                    continue
                x, y = i, j
                num = ''
                while 0 <= x < N and 0 <= y < M:
                    num += A[x][y]
                    n = int(num)
                    root = int(n ** 0.5)
                    if root * root == n:
                        ans = max(ans, n)
                    x += dx
                    y += dy
print(ans)