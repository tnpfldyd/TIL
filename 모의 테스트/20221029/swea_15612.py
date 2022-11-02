T = int(input())
dx, dy = [0,0,1,-1], [1,-1,0,0]
for i in range(1, T+1):
    matrix = [list(input()) for _ in range(8)]
    cnt = 0
    answer = True
    for j in range(8):
        for k in range(8):
            if matrix[j][k] == 'O':
                cnt += 1
                for l in range(4):
                    nx, ny = j + dx[l], k + dy[l]
                    while 0 <= nx < 8 and 0 <= ny < 8:
                        if matrix[nx][ny] == 'O':
                            answer = False
                            break
                        else:
                            nx, ny = nx + dx[l], ny + dy[l]
    if cnt == 8 and answer:
        print(f'#{i} yes')
    else:
        print(f'#{i} no')