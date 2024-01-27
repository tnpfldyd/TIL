from itertools import permutations
import sys
input = sys.stdin.readline

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_prime_permutations(digits):
    primes = set()
    for i in range(1, len(digits) + 1):
        for perm in permutations(digits, i):
            num = int("".join(perm))
            if is_prime(num):
                primes.add(num)
    return len(primes)

T = int(input())
for _ in range(T):
    digits = input().strip()
    result = count_prime_permutations(digits)
    print(result)