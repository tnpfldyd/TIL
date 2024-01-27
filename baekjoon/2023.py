N = int(input())

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def recursive(cur, n):
    if n == 0:
        print(cur)
        return

    for i in range(1, 10, 2):
        tmp = cur * 10 + i
        if is_prime(tmp):
            recursive(tmp, n - 1)

prime = [2, 3, 5, 7]

for i in range(4):
    recursive(prime[i],  N - 1)
