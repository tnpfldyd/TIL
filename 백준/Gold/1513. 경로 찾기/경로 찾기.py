import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

mod = 1000007

def go(y, x, cnt, prev):
    if y > n or x > m:
        return 0
    if y == n and x == m:
        if cnt == 0 and a[y][x] == 0:
            return 1
        if cnt == 1 and a[y][x] > prev:
            return 1
        return 0
    
    if dp[y][x][cnt][prev] != -1:
        return dp[y][x][cnt][prev]
    
    ret = 0
    if a[y][x] == 0:
        ret = (go(y + 1, x, cnt, prev) + go(y, x + 1, cnt, prev)) % mod
    elif a[y][x] > prev:
        ret = (go(y + 1, x, cnt - 1, a[y][x]) + go(y, x + 1, cnt - 1, a[y][x])) % mod
    
    dp[y][x][cnt][prev] = ret
    return ret

n, m, c = map(int, input().split())

a = [[0] * (m + 1) for _ in range(n + 1)]
dp = [[[[-1] * (c + 1) for _ in range(c + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, c + 1):
    y, x = map(int, input().split())
    a[y][x] = i

for i in range(c + 1):
    print(go(1, 1, i, 0), end=" ")