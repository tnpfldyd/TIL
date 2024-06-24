memoization = {1: 1, 2: 1, 3: 2, 4: 3, 5: 5}

def fibonacci(n):
    if n in memoization:
        return memoization[n]
    else:
        if n % 2 == 1:
            memoization[n] = (fibonacci(n // 2) ** 2 + fibonacci(n // 2 + 1) ** 2) % 1000000000
        else:
            memoization[n] = (fibonacci(n + 1) - fibonacci(n - 1)) % 1000000000
        return memoization[n]

a, b = map(int, input().split())
result = (fibonacci(b + 2) - fibonacci(a + 1)) % 1000000000
print(result)
