import sys

def matrix_multiply(A, B, mod):
    N = len(A)
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % mod
    return result

def matrix_pow(A, B, mod):
    N = len(A)
    result = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    
    base = A[:]
    
    while B > 0:
        if B % 2 == 1:
            result = matrix_multiply(result, base, mod)
        base = matrix_multiply(base, base, mod)
        B //= 2
    
    return result

def main():
    input = sys.stdin.readline
    N, B = map(int, input().split())
    
    A = []
    for _ in range(N):
        row = list(map(int, input().split()))
        A.append(row)
    
    mod = 1000
    
    result = matrix_pow(A, B, mod)
    
    for row in result:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
