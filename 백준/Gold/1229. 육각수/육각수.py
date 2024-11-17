def main():
    Max = 900
    n = int(input())
    six = [0] * Max
    dp = [float('inf')] * (n + 1)

    six[1] = 1
    dp[0] = 0

    for i in range(1, n + 1):
        dp[i] = 6

    for i in range(2, Max):
        six[i] = six[i - 1] + i * 4 - 3

    for i in range(1, n + 1):
        for j in range(1, Max):
            if i >= six[j]:
                dp[i] = min(dp[i], dp[i - six[j]] + 1)
            else:
                break

    print(dp[n])

if __name__ == "__main__":
    main()