def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if not n % p:
            while not n % p:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

n = int(input())
print(phi(n))