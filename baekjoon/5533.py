import sys
input = sys.stdin.readline
T = int(input().rstrip())
matrix = [list(map(int, input().rstrip().split())) for _ in range(T)]
result = []
result2 = []
cnt_result = []
for j in range(3):
    for i in range(T):
        result.append(matrix[i][j])
        if i == T-1:
            result2.append(result)
            result = []
for i in range(T):
    cnt = 0
    for j in range(3):
        if result2[j].count(result2[j][i]) == 1:
            cnt += result2[j][i]
    cnt_result.append(cnt)
print(*cnt_result, sep='\n')