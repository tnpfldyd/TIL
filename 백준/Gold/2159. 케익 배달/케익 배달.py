import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = float('inf')
dx = [0, 0, 1, 0, -1]
dy = [0, 1, 0, -1, 0]

def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def f(i, j, x, y):
    if i == n:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    
    ret = INF
    for k in range(5):
        nx = points[i + 1][0] + dx[k]
        ny = points[i + 1][1] + dy[k]
        ret = min(ret, f(i + 1, k, nx, ny) + get_dist(x, y, nx, ny))
    
    dp[i][j] = ret
    return ret

if __name__ == "__main__":
    n = int(input())
    dp = [[-1] * 5 for _ in range(n + 1)]
    points = [tuple(map(int, input().split())) for _ in range(n + 1)]

    print(f(0, 0, points[0][0], points[0][1]))