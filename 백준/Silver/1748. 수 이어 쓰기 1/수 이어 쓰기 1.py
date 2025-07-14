def count_digits(n):
    if n == 0:
        return 0
    
    total_digits = 0
    digits = 1
    start = 1
    
    while start <= n:
        end = min(n, start * 10 - 1)
        count = end - start + 1
        total_digits += count * digits
        start *= 10
        digits += 1
    
    return total_digits

n = int(input())
print(count_digits(n))