from math import factorial as f

def binomial_coefficient(n, k):
    return f(n) // (f(k) * f(n - k))

def calculate_combinations(N, K):
    combinations = binomial_coefficient(N, K) * (2 ** (K - 1))
    return combinations % MOD

N, K = map(int, input().split())
MOD = int(1e9 + 7)
input()
result = calculate_combinations(N, K)
print(result)