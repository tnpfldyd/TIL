import sys
input = sys.stdin.readline

def f(x, y, n):
    v = a[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if a[i][j] != v:
                m = n//2
                return '(' + f(x, y, m) + f(x, y+m, m) + f(x+m, y, m) + f(x+m, y+m, m) + ')'
    return v

N = int(input())
a = [list(input().strip()) for _ in range(N)]
print(f(0, 0, N))