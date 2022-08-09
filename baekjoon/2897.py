R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
result = [] # 들어갈수 있는 자리 모두 입력
dx, dy = [0,1,1], [1,1,0] # 2행 2열 자리에 들어가므로 3자리만 검사
for x in range(R):
    for y in range(C):
        temp = []
        if matrix[x][y] != '#': # 검사 시작 위치가 빌딩(#) 이면 제외
            temp.append(matrix[x][y]) 
            for k in range(3):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < R and 0 <= ny < C:
                    temp.append(matrix[nx][ny])
        if len(temp) == 4: # 총 2행 2열 = 4칸 짜리만 result에 입력
            result.append(temp)
cnt = [0] * 5
for i in result:
    X = 0
    if '#' in i: # i 안에 # 이 있으면 통과하고 다음꺼 진행
        continue
    for j in i:
        if 'X' == j: # 벽(X) 의 갯수 대로 X 카운트
            X += 1
    cnt[X] += 1 # 벽의 갯수 자리에 카운트 +1
for i in cnt:
    print(i)