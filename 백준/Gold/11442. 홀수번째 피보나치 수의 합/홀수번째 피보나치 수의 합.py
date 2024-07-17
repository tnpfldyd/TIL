n = (int(input()) + 1) // 2 * 2
a = [[1, 1], [1, 0]]
b = [[1, 0], [0, 1]]
MOD = 1000000007
def mul(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= MOD
    return result

while n:
    if n & 1:
        b = mul(b, a)
    a = mul(a, a)
    n //= 2

print(b[1][0])