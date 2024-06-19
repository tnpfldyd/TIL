def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

def get_digit(number, position):
    return (number // power(10, position - 1)) % 10

n, k = map(int, input().split())

remaining_k = 0
current_position = 0
while k > 0:
    remaining_k = k
    current_position += 1
    k -= (9 * current_position * power(10, current_position - 1))

target_number = power(10, current_position - 1) + (remaining_k - 1) // current_position
result = get_digit(target_number, current_position - (remaining_k - 1) % current_position)

print(-1 if target_number > n else result)
