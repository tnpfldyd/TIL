def get_calculation(x):
    return (x.count('1') + 1) // 2

a, b = get_calculation(input()), get_calculation(input())
print('VICTORY' if a >= b else 'DEFEAT')