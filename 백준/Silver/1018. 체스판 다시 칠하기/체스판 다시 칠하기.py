n, m = map(int, input().split()) # 보드의 크기 입력 받기
board = [] # 보드 정보를 저장할 리스트

# 보드 정보 입력 받기
for i in range(n):
    row = input()
    board.append(row)

min_count = 64 # 최소로 다시 칠해야 하는 정사각형의 개수를 저장할 변수, 최대값으로 초기화

# (0,0)을 시작으로 하여 8x8 크기의 체스판으로 만들 수 있는 모든 경우에 대해 검사
for i in range(n-7):
    for j in range(m-7):
        count1, count2 = 0, 0 # 첫 칸이 흰색인 경우와 검은색인 경우 각각에 대해 다시 칠해야 하는 정사각형의 개수를 저장할 변수
        for x in range(i, i+8):
            for y in range(j, j+8):
                # 첫 칸이 흰색인 경우와 검은색인 경우 각각에 대해 다시 칠해야 하는 정사각형의 개수 계산
                if (x+y)%2 == 0: # 행 번호와 열 번호의 합이 짝수인 경우 흰색이어야 함
                    if board[x][y] == 'B':
                        count1 += 1
                    else:
                        count2 += 1
                else: # 행 번호와 열 번호의 합이 홀수인 경우 검은색이어야 함
                    if board[x][y] == 'W':
                        count1 += 1
                    else:
                        count2 += 1
        # 첫 칸이 흰색인 경우와 검은색인 경우 중에서 더 작은 값을 min_count와 비교하여 최소값 업데이트
        min_count = min(min_count, count1, count2)

print(min_count)