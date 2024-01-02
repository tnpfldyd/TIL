n = int(input())
answer = 1
MOD = 10007
while n >= 5:
    answer *= 3
    answer %= MOD
    n -= 3

print((answer * n) % MOD)