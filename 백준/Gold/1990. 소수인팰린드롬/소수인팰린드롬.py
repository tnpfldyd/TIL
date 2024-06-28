def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]

def find_palindrome_primes(a, b):
    palindrome_primes = []
    for num in range(a, min(b + 1, 10000000)):
        if is_palindrome(num) and is_prime(num):
            palindrome_primes.append(num)
    return palindrome_primes

a, b = map(int, input().split())
palindrome_primes = find_palindrome_primes(a, b)

for num in palindrome_primes:
    print(num)
print(-1)
