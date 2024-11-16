def is_prime(num):
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

n = int(input())
prime = []

for i in range(2, n+1):
    if is_prime(i):
        prime.append(i)

dp = [0 for _ in range(n+1)]
dp[0] = 1
for p in prime:
    for i in range(p, n+1):
        dp[i] = (dp[i] + dp[i-p]) % 123456789
            
print(dp[n])