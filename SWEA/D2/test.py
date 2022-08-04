def rotated(rotation):
    rotation_90 = zip(*rotation[::-1])
    return rotation_90
for i in range(1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    matrix_90 = rotated(matrix)
    for i in range(3):
        print(''.join(map(str, matrix_90[i])), end = ' ')