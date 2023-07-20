target = int(input())
start = 1
digit = 1
result = [0] * 10

def counting(number, digit):
    while number:
        result[number % 10] += digit
        number //= 10
while start <= target:
    while start % 10 and start <= target:
        counting(start, digit)
        start += 1
    if target < start:
        break
    while target % 10 != 9 and start <= target:
        counting(target, digit)
        target -= 1
    start //= 10; target //= 10
    for i in range(10):
        result[i] += (target - start + 1) * digit
    digit *= 10
print(*result)