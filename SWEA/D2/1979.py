import sys

sys.stdin = open("1979input.txt", "r")
T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    row = 0
    for x in range(N):
        cnt = 0
        for y in range(N):
            if matrix[x][y] == 1:
                cnt += 1
            else:
                if cnt == M:
                    row += 1
                cnt = 0
        if cnt == M:
            row += 1
    col = 0
    for x in range(N):
        cnt = 0
        for y in range(N):
            if matrix[y][x] == 1:
                cnt += 1
            else:
                if cnt == M:
                    col += 1
                cnt = 0
        if cnt == M:
            col += 1
    print(f'#{i}', row+col)

