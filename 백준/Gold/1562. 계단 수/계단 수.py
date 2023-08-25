N = int(input())
MOD = 1000000000

dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N+1)]

def bit(length, num, state):
    if length == N:
        return 1 if state == (1 << 10) - 1 else 0
    if dp[length][num][state]:
        return dp[length][num][state]
    
    cnt = 0
    if num:
        cnt += bit(length + 1, num - 1, state | (1 << (num - 1)))
    if num < 9:
        cnt += bit(length + 1, num + 1, state | (1 << (num + 1)))
    
    dp[length][num][state] = cnt % MOD
    return dp[length][num][state]

result = 0
for i in range(1, 10):
    result += bit(1, i, 1 << i)
    result %= MOD

print(result)