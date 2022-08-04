import sys

sys.stdin = open("1961input.txt", "r")
T = int(input())
def rotated(X, N):
    mat_90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            mat_90[i][j] = X[N-1-j][i]
    return mat_90
for i in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    matrix_90 = rotated(matrix, N)
    matrix_180 = rotated(matrix_90, N)
    matrix_270 = rotated(matrix_180, N)
    print(f'#{i}')
    for j in range(N):
        print(''.join(map(str, matrix_90[j])), end= ' ')
        print(''.join(map(str, matrix_180[j])), end= ' ')
        print(''.join(map(str, matrix_270[j])), end= ' ')
        print()
