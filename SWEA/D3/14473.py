T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    sharpvisited = [[False] * M for _ in range(N)] # 샵이 짝수일때
    jumvisited = [[False] * M for _ in range(N)] # 점이 짝수일때
    for j in range(N):
        for k in range(M):
            if (j + k) % 2 == 0:
                if matrix[j][k] == '#':
                    sharpvisited[j][k] = True
                else:
                    jumvisited[j][k] = True
            else:
                if matrix[j][k] == '.':
                    sharpvisited[j][k] = True
                else:
                    jumvisited[j][k] = True
            if matrix[j][k] == '?':
                sharpvisited[j][k] = True
                jumvisited[j][k] = True
    print(f'#{i}','possible' if max(sum(map(sum, sharpvisited)),sum(map(sum, jumvisited))) == N * M else 'impossible')
