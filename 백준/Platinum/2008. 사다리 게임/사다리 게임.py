import sys
input = sys.stdin.readline
INF = sys.maxsize
M, N = map(int, input().split())
start, end, del_cost, add_cost = map(int, input().split())
start -= 1; end -= 1
P = [0] * (N + 1) # i번째 가로선이 세로선 i 와 i + 1을 연결함
for i in range(1, N + 1):
    p = int(input()) - 1
    P[i] = p
matrix = [[INF] * (M + 1) for _ in range(N + 1)] # matrix[x][y] 에서 x는 연결된 가로선의 갯수, y는 위치
for i in range(M): # 시작점과 다른 위치에 있는 세로선의 비용 계산
    if i == start:
        matrix[0][i] = 0
        continue
    matrix[0][i] = abs(start - i) * add_cost

#i개의 가로선을 추가하고 j위치에 있는 세로선으로 이동할 때의 최소 비용 계산
for i in range(1, N + 1): # 고려하는 가로선
    for j in range(M): # 시작점
        for k in range(M): # 도착점
            if j == k and (P[i] == k or P[i] + 1 == k): # 시작점과 도착점이 같고 P[i] 가로선이 도착점이거나 P[i] + 1 이 도착점이면 해당 가로선을 제거하여 비용 계산
                nx = matrix[i-1][k] + del_cost
                if matrix[i][j] > nx:
                    matrix[i][j] = nx
            elif (k <= P[i] and P[i] <= j-1) or (j <= P[i] and P[i] <= k-1): # 가로선을 k에서 j-1에 추가할 수 있는 경우 혹은 j에서 k-1 사이에 추가할 수 있는 경우
                nx = matrix[i-1][k] + (abs(k-j)-1) * add_cost # 가로선을 추가하여 비용 계산
                if matrix[i][j] > nx:
                    matrix[i][j] = nx
            else:
                nx = matrix[i-1][k] + abs(k-j) * add_cost # 직접 이동하는 비용 계산
                if matrix[i][j] > nx:
                    matrix[i][j] = nx
print(matrix[N][end])

