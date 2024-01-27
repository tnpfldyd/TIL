N = int(input())
matrix = [[False] * (N + 1) for _ in range(N + 1)]

matrix[1][N] = matrix[N][1] = True

answer = []
prev = 0

for _ in range(N * (N - 1) // 2):
    for cur in range(1, N + 1):
        if cur == prev or matrix[cur][prev]:
            continue
        matrix[cur][prev] = matrix[prev][cur] = True
        prev = cur
        break
    answer.append(f'a{prev}')
answer.append('a1')

print(*answer)
