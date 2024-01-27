import sys
INF = sys.maxsize
DNA = input()
N = len(DNA)

dp = [[INF] * N for _ in range(N)]

def td(l, r):
    if l > r: return 0
    if l == r: return 1
    if dp[l][r] != INF:
        return dp[l][r]
    if (DNA[l] == 'a' and DNA[r] == 't') or (DNA[l] == 'g' and DNA[r] == 'c'):
        dp[l][r] = min(dp[l][r], td(l + 1, r - 1))
    for i in range(l, r):
        dp[l][r] = min(dp[l][r], td(l, i) + td(i + 1, r))
    return dp[l][r]

print(N - td(0, N - 1))