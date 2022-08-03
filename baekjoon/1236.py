import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
matrix = [list(input().rstrip()) for _ in range(N)]
cnt = 0
Xcnt = 0
result = []
for i in range(N):
    if 'X' not in matrix[i]:
        Xcnt += 1
for j in range(M):
    for i in range(N):
        result.append(matrix[i][j])
        if i == N-1:
            if 'X' not in result:
                cnt += 1
                result = []
            else:
                result = []
print(Xcnt if Xcnt > cnt else cnt)