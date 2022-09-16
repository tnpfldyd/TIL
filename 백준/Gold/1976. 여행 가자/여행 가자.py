import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
INF = sys.maxsize
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 0 and i != j:
            matrix[i][j] = INF
for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]
num_list = list(map(int, input().rstrip().split()))
answer = True
for i in range(len(num_list)-1):
    if matrix[num_list[i]-1][num_list[i+1]-1] >= INF:
        answer = False
        break
print('YES' if answer else 'NO')