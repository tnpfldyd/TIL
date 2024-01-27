number = input().strip() + '0'
dp = [0] * 45
dp[0] = 1

for i in range(len(number) - 1):
    number_digit = int(number[i])
    if number_digit:
        dp[i + 1] += dp[i]
        if 10 <= number_digit * 10 + int(number[i + 1]) <= 34:
            dp[i + 2] += dp[i]

print(dp[len(number) - 1])