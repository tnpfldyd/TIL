result = [[0] * 15 for i in range(5)]
for i in range(5):
    d = list(input())
    for j in range(len(d)):
        result[i][j] = d[j]
for i in range(15):
    for j in range(5):
        if result[j][i] == 0:
            continue
        else:
            print(result[j][i], end='')