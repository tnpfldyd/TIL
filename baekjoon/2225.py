def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n, r = map(int, input().split())
combination = factorial(n + r - 1) // (factorial(r - 1) * factorial(n))
result = combination % 1000000000
print(result)