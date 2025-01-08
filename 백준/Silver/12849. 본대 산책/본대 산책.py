D = int(input())
MOD = 1000000007

dp = [0] * 8
dp[0] = 1

connections = [
    [1, 2],
    [0, 2, 3],
    [0, 1, 3, 4],
    [1, 2, 4, 5],
    [2, 3, 5, 6],
    [3, 4, 7],
    [4, 7],
    [5, 6],
]

for _ in range(D):
    tmp = [0] * 8
    for i in range(8):
        tmp[i] = sum(dp[j] for j in connections[i]) % MOD
    dp = tmp

print(dp[0])