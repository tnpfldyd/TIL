import sys
input = sys.stdin.readline

def set_bomb_effect(data_matrix):
    new_matrix = [[0 for _ in range(N - M + 1)] for _ in range(N - M + 1)]

    for row in range(N - M + 1):
        for col in range(N - M + 1):
            new_matrix[row][col] = -data_matrix[row][col]

    return new_matrix

N, M = map(int, input().split())

height_map = [list(map(int, input().split())) for _ in range(N)]

height_map = set_bomb_effect(height_map)

sum_matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

result_matrix = [[0 for _ in range(N - M + 1)] for _ in range(N - M + 1)]

for row in range(N - M + 1):
    for col in range(N - M + 1):
        result_matrix[row][col] = height_map[row][col] - sum_matrix[row][col] + sum_matrix[row + M][col] + sum_matrix[row][col + M] - sum_matrix[row + M - 1][col + M] - sum_matrix[row + M][col + M - 1] + sum_matrix[row + M - 1][col + M - 1]
        sum_matrix[row + M][col + M] = sum_matrix[row + M - 1][col + M] + sum_matrix[row + M][col + M - 1] - sum_matrix[row + M - 1][col + M - 1] + result_matrix[row][col]

for i in range(M // 2):
    print("0 " * N)

for row in range(N - M + 1):
    print("0 " * (M // 2) + " ".join(map(str, result_matrix[row])) + " 0" * (M // 2))

for i in range(M // 2):
    print("0 " * N)