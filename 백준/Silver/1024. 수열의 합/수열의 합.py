N, L = map(int, input().split())

found = False
for length in range(L, 101):
    numerator = 2 * N - length * (length - 1)
    denominator = 2 * length
    if numerator % denominator != 0:
        continue
    a = numerator // denominator
    if a < 0:
        continue
    result = [str(a + i) for i in range(length)]
    print(" ".join(result))
    found = True
    break

if not found:
    print(-1)