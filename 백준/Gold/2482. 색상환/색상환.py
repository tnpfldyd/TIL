MOD = 1000000003

def main():
    N, K = int(input()), int(input())
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    for i in range(N + 1):
        dp[i][1] = i
        dp[i][0] = 1
    
    for i in range(2, N + 1):
        for j in range(2, K + 1):
            dp[i][j] = (dp[i - 2][j - 1] + dp[i - 1][j]) % MOD
    
    answer = (dp[N - 1][K] + dp[N - 3][K - 1]) % MOD
    print(answer)

if __name__ == "__main__":
    main()
