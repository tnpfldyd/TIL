import sys
input = sys.stdin.readline
N, M = map(int, input().split())

def solve(n, m):
    if not m:
        return False
    elif n > m * 2:
        return True
    a, b = max(m, n % m), min(m, n % m)
    return not solve(a, b)

print('win' if solve(max(N, M), min(N, M)) else 'lose')