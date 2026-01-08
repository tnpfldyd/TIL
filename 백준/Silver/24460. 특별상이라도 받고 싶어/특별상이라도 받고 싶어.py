import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

def solve(x, y, size):
    if size == 1:
        return A[x][y]

    half = size // 2
    vals = [
        solve(x, y, half),
        solve(x, y + half, half),
        solve(x + half, y, half),
        solve(x + half, y + half, half),
    ]
    vals.sort()
    return vals[1]

print(solve(0, 0, N))