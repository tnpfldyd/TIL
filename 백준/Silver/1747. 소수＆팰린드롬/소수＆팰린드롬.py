def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_palindrome_prime(n):
    current = n
    while True:
        if is_palindrome(current) and is_prime(current):
            return current
        current += 1

n = int(input())
result = find_palindrome_prime(n)
print(result)