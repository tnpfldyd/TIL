def factorize(N):
    factors = []
    divisor = 2
    remaining = N
    
    while remaining > 1 and divisor * divisor <= N:
        if remaining % divisor == 0:
            factors.append(divisor)
            remaining //= divisor
        else:
            divisor += 1
    
    if remaining > 1:
        factors.append(remaining)
    
    return factors

N = int(input())
prime_factors = factorize(N)

if len(prime_factors) < 2:
    print(-1)
else:
    result = []
    for i in range(1, len(prime_factors), 2):
        if i == len(prime_factors) - 2:
            result.append(prime_factors[i] * prime_factors[i-1] * prime_factors[i+1])
        else:
            result.append(prime_factors[i] * prime_factors[i-1])
    
    print(*result)