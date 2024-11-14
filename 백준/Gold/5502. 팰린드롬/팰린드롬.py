def main():
    M = 5001
    dp = [[0] * M for _ in range(M)]

    answer = 0
    N = int(input())
    s1 = input().strip()
    s2 = s1[::-1]

    s1 = ' ' + s1
    s2 = ' ' + s2

    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                answer = max(answer, dp[i][j])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(N - dp[N][N])

if __name__ == "__main__":
    main()