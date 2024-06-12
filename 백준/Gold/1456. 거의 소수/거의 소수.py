A, B = map(int, input().split())

is_prime = [True] * (int(B ** 0.5) + 1)
is_prime[1] = False

for i in range(2, int(B ** 0.5) + 1):
    if is_prime[i]:
        if i * i > int(B ** 0.5):
            break
        for j in range(i**2, int(B ** 0.5) + 1, i):
            is_prime[j] = False

count = 0
for i in range(1, len(is_prime)):
    if is_prime[i]:
        current_num = i * i
        while True:
            if current_num < A:
                current_num *= i
                continue
            if current_num > B:
                break
            current_num *= i
            count += 1

print(count)
