import sys
input = sys.stdin.readline
matrix = [list(map(int, input().rstrip().split())) for _ in range(19)]
low = [1,1,0,-1]# 맨 좌측에 있는 돌 기준으로 해야 하기때문에 4방향만 검사 아래, 우하, 우, 우상 순으로 검사
col = [0,1,1,1]
for x in range(19):
    for y in range(19):
        if matrix[x][y] != 0: # 0이아니라 1이나 2가 걸렸을때 4방향 검사
            for k in range(4):
                nx = x + low[k]
                ny = y + col[k]
                cnt = 1
                while 0 <= nx < 19 and 0 <= ny < 19 and matrix[nx][ny] == matrix[x][y]: # 정상 인덱스 범위 안에 있을때, nx,ny가 x,y와 같다면 실행
                    cnt += 1
                    if cnt == 5: # 오목이 됐을때 6목 검사
                        if 0 <= x - low[k] < 19 and 0 <= y - col[k] < 19 and matrix[x - low[k]][y - col[k]] == matrix[x][y]: # 역으로 갔을때, 정상적인 인덱스 범위 안에있을때
                            break
                        if 0 <= nx + low[k] < 19 and 0 <= ny + col[k] < 19 and matrix[nx + low[k]][ny + col[k]] == matrix[x][y]: # 한칸 더 갔을때, 정상적인 인덱스 범위 안에 있을때 
                            break
                        print(matrix[x][y]) # 6목이 아니면 결과 값 출력
                        print(x + 1, y + 1) # 0,0 이아니라 1,1 부터 시작이기때문에 +1
                        sys.exit(0) # 출력이 됐을때 코드들 실행 금지
                    nx += low[k] # 정해진 방향이 똑같은 숫자 일 때 그 방향 그대로 더하면서 while 문으로 검사
                    ny += col[k]
print(0) # 위에서 출력이 안됐을 시 승부가 안났으므로 0 출력
