import sys
input = sys.stdin.readline

def chess(color):
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(M):
            if not (i + j) % 2:
                value = 1 if board[i][j] != color else 0
            else:
                value = 1 if board[i][j] == color else 0

            prefix_sum[i + 1][j + 1] = prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j] + value

    result = float('inf')

    for i in range(N - K + 1):
        for j in range(M - K + 1):
            temp = prefix_sum[i + K][j + K] - prefix_sum[i][j + K] - prefix_sum[i + K][j] + prefix_sum[i][j]
            result = min(temp, result)

    return result


N, M, K = map(int, input().split())
board = [input().strip() for _ in range(N)]

result = min(chess('B'), chess('W'))
print(result)