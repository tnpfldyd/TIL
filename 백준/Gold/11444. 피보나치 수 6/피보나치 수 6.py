MOD = 1000000007

def matrix_mult(A, B):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]]

def matrix_power(matrix, n):
    result = [[1, 0], [0, 1]]
    base = matrix

    while n > 0:
        if n % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        n //= 2

    return result

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    F = [[1, 1],
         [1, 0]]

    F_n_minus_1 = matrix_power(F, n-1)
    return F_n_minus_1[0][0]

N = int(input())

print(fibonacci(N))
