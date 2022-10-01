for i in range(1, 11):
    a = int(input())
    max_num = 0
    matrix = [list(map(int, input().split())) for _ in range(100)]
    for j in range(100):
        max_num = max(max_num, sum(matrix[j]))
    temp = 0
    for j in range(100):
        temp += matrix[j][j]
    max_num = max(max_num, temp)
    cnt = 0
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += matrix[j][i]
            if i + j == 99:
                cnt += matrix[i][j]
        max_num = max(max_num, temp)
    max_num = max(max_num, cnt)
    print(f'#{a} {max_num}')