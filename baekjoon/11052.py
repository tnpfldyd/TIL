N = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)
def topDown(n):
    if not n:
        return 0
    if dp[n]:
        return dp[n]
    
    ret = 0
    for i in range(1, n+1):
        temp = topDown(n-i) + cards[i]
        ret = max(ret, temp)
    dp[n] = ret
    return ret
print(topDown(N))