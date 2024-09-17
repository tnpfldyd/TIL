import sys
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
dp = [[[[False for _ in range(450)] for _ in range(31)] for _ in range(31)] for _ in range(31)]
ans = [''] * 31

def solve(n, a, b, p):
    if n == N:
        if p == K:
            print(''.join(ans))
            sys.exit(0)
        return False

    if dp[n][a][b][p]:
        return False
    
    dp[n][a][b][p] = True

    for char, new_a, new_b, new_p in [('A', a+1, b, p), ('B', a, b+1, p+a), ('C', a, b, p+a+b)]:
        ans[n] = char
        solve(n+1, new_a, new_b, new_p)

    return False

solve(0, 0, 0, 0)
print(-1)