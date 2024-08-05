def calculate_population(a, b, d, n):
    dp = [0] * (n + 1)

    for i in range(a):
        dp[i] = 1

    for i in range(a, n + 1):
        dp[i] = (dp[i - 1] + dp[i - a]) % 1000
        if b <= i:
            dp[i] = (dp[i] - dp[i - b] + 1000) % 1000

    answer = dp[n]
    if n >= d:
        answer = (answer + 1000 - dp[n - d]) % 1000

    return answer

a, b, d, n = map(int, input().split())
result = calculate_population(a, b, d, n)
print(result)
