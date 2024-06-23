N, K = map(int, input().split())
MOD = 1000000007

def calculate_factorial(n):
    result = 1
    for i in range(2, n+1):
        result = (result * i) % MOD
    return result

def calculate_power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    
    tmp = calculate_power(base, exponent//2)
    if exponent % 2:
        return tmp * tmp * base % MOD
    else:
        return tmp * tmp % MOD

numerator = calculate_factorial(N)
denominator = (calculate_factorial(N-K) * calculate_factorial(K)) % MOD

result = numerator * calculate_power(denominator, MOD-2) % MOD
print(result)
