import sys, itertools
INF = 2000
input = sys.stdin.readline
N, T = map(int, input().split())
matrix = [[INF] * N for _ in range(N)]
result = []
for i in range(N):
    s, x, y = map(int, input().split())
    result.append([i, s, x, y])
for a, b in itertools.combinations(result, 2):
    cnt = abs(a[2] - b[2]) + abs(a[3] - b[3]) # 여러번 쓰는 값은 미리 값 구해두기
    if a[1] == 1 and b[1] == 1:
        matrix[a[0]][b[0]] = min(T, cnt)
        matrix[b[0]][a[0]] = min(T, cnt)
    else:
        matrix[a[0]][b[0]] = cnt
        matrix[b[0]][a[0]] = cnt
for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]: # min 보다 if 가 빠름
                matrix[i][j] = matrix[i][k] + matrix[k][j]
case = int(input())
for i in range(case):
    a, b = map(int, input().split())
    if a == b:
        print(0)
    else:
        print(matrix[a-1][b-1])