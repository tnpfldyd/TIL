import sys
from pprint import pprint

# sys.stdin = open("14502.txt", "r")

# 판 만들기
N, M = map(int, input().split())
board = []
for _ in range(N):
    data = input().split(" ")
    board.append(data)

# 4방위 탐색
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


# 바이러스 퍼트리기
def virus(a, b):

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx and nx < N and 0 <= ny and ny < M and board[nx][ny] == "0":
            # 퍼진 바이러스는 3으로 표시
            board[nx][ny] = "3"
            virus(nx, ny)


# 첫번쨰 두번째 세번째 벽을 관리하기 위해
stack1 = [0]
stack2 = [0]
stack3 = [0]
# 크기 카운트
cnt = 0
# 최대값 저장
max_ = 0
# 첫번째 벽
for aa in range(N * M):
    a = aa // M
    b = aa % M
    if board[a][b] == "0":
        delete = stack1.pop()
        if delete != 0:
            board[delete[0]][delete[1]] = "0"

        board[a][b] = "1"
        stack1.append((a, b))
    else:
        continue
    # 두번째 벽
    for cc in range(aa + 1, N * M):
        c = cc // M
        d = cc % M

        if board[c][d] == "0":
            delete = stack2.pop()
            if delete != 0:
                board[delete[0]][delete[1]] = "0"

            board[c][d] = "1"
            stack2.append((c, d))
        else:
            continue
        # 세번째 벽
        for ee in range(cc + 1, N * M):
            e = ee // M
            f = ee % M

            if board[e][f] == "0":
                delete = stack3.pop()
                if delete != 0:
                    board[delete[0]][delete[1]] = "0"

                board[e][f] = "1"
                stack3.append((e, f))

                # 바이러스 탐색 및 퍼트리기
                for i in range(N):
                    for j in range(M):
                        if board[i][j] == "2":
                            # 퍼진 바이러스는 "3"을 줘서 바이러스 "2"와 구분
                            virus(i, j)
                # 크기 카운터 및 원상복구
                for i in range(N):
                    for j in range(M):
                        if board[i][j] == "0":
                            cnt += 1
                        elif board[i][j] == "3":
                            board[i][j] = "0"
                # 최대값
                if max_ < cnt:
                    max_ = cnt
                cnt = 0
            else:
                continue

print(max_)