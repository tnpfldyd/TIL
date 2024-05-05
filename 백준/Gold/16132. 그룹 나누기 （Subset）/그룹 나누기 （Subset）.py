def f(cur, n):
    if cur > N or n > S:
        return 0
    if n == S:
        return 1
    if dp[cur][n] != -1:
        return dp[cur][n]
    ret = 0
    ret = f(cur + 1, n) + f(cur + 1, n + cur)
    dp[cur][n] = ret
    return ret

N = int(input())
S = N * (N + 1) // 2
if S % 2:
    print(0)
else:
    S //= 2
    dp = [[-1] * 638 for _ in range(51)]
    print(f(1, 0))