import sys
input = sys.stdin.readline

def get_int_input():
    a, b = map(float, input().split())
    return int(a), int(b * 100 + 0.5)

while True:
    N, M = get_int_input()
    if not N and not M:
        break

    dp = [0] * (M + 1)
    for _ in range(N):
        c, p = get_int_input()
        
        for j in range(p, M + 1):
            dp[j] = max(dp[j], dp[j - p] + c)
    
    print(dp[M])