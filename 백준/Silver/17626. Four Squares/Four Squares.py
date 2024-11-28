n = int(input())
is_square = [0 if i**0.5 % 1 else 1 for i in range(n + 1)]

min_count = 4
for i in range(int(n**0.5), 0, -1):
    if is_square[n]:
        min_count = 1
        break
    elif is_square[n - i**2]:
        min_count = 2
        break
    else:
        for j in range(int((n - i**2)**0.5), 0, -1):
            if is_square[(n - i**2) - j**2]:
                min_count = 3
                break

print(min_count)