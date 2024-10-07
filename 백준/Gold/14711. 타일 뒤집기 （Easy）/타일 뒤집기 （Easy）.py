import sys

input = sys.stdin.readline

N = int(input())
map_data = [['.'] * N for _ in range(N)]
check = [[0] * N for _ in range(N)]

map_data[0] = list(input().strip())
print(''.join(map_data[0]))

for i in range(N - 1):
    for j in range(N):
        if map_data[i][j] == '#':
            check[i][j] += 1
            for dr, dc in [(0, -1), (0, 1), (1, 0)]:
                nr, nc = i + dr, j + dc
                if 0 <= nr < N and 0 <= nc < N:
                    check[nr][nc] += 1

    for j in range(N):
        if check[i][j] % 2 == 0:
            map_data[i+1][j] = map_data[i][j]
        else:
            map_data[i+1][j] = '#' if map_data[i][j] == '.' else '.'
    
    print(''.join(map_data[i+1]))

sys.stdout.flush()