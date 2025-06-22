import sys
input = sys.stdin.readline

N = int(input())
b = [list(input().strip()) for _ in range(N)]
res = 0

def check():
    m = 0
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if b[i][j] == b[i][j-1]:
                cnt += 1
            else:
                m = max(m, cnt)
                cnt = 1
        m = max(m, cnt)
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if b[i][j] == b[i-1][j]:
                cnt += 1
            else:
                m = max(m, cnt)
                cnt = 1
        m = max(m, cnt)
    return m

for i in range(N):
    for j in range(N):
        if j+1 < N and b[i][j] != b[i][j+1]:
            b[i][j], b[i][j+1] = b[i][j+1], b[i][j]
            res = max(res, check())
            b[i][j], b[i][j+1] = b[i][j+1], b[i][j]
        if i+1 < N and b[i][j] != b[i+1][j]:
            b[i][j], b[i+1][j] = b[i+1][j], b[i][j]
            res = max(res, check())
            b[i][j], b[i+1][j] = b[i+1][j], b[i][j]

print(res)