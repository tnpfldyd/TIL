MOD = 1000000007

def main():
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    dp = [[0] * 5001 for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        if arr[i] >= 5000:
            print(0)
            return

    if arr[1] > 0 or arr[N] > 0:
        print(0)
        return

    dp[1][0] = 1
    arr[N] = 0

    for i in range(2, N + 1):
        if arr[i] == -1:
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
            for k in range(1, 5000):
                dp[i][k] = (dp[i - 1][k - 1] + dp[i - 1][k] + dp[i - 1][k + 1]) % MOD
        else:
            if arr[i] == 0:
                dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
            else:
                dp[i][arr[i]] = (dp[i - 1][arr[i] - 1] + dp[i - 1][arr[i]] + dp[i - 1][arr[i] + 1]) % MOD

    print(dp[N][0])

if __name__ == "__main__":
    main()