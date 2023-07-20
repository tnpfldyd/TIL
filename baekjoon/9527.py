MAX = 55

def getOne(x):
    ret = x & 1

    for i in range(MAX - 1, 0, -1):
        if x & (1 << i):
            ret += power2[i - 1] + (x - (1 << i) + 1)
            x -= 1 << i

    return ret

A, B = map(int, input().split())

power2 = [0] * MAX
power2[0] = 1
for i in range(1, MAX):
    power2[i] = 2 * power2[i - 1] + (1 << i)

print(getOne(B) - getOne(A - 1))