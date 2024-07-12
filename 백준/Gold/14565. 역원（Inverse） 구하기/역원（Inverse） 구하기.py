def euclid(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x, 1, 0

    g, x1, y1 = euclid(y, x % y)
    return g, y1, x1 - (x // y) * y1

n, a = map(int, input().split())

print(n - a, end=" ")

g, x, y = euclid(n, a)

if g != 1:
    print(-1)
else:
    print((y + n) % n)
