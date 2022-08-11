# 실패
import sys
# input = sys.stdin.readline
sys.stdin = open('2580input.txt', 'r')
def low(low):
    yx = []
    for x in range(9):
        reee = []
        for y in range(9):
            reee.append(low[y][x])
        yx.append(reee)
    return yx
def x3x(x3x):
    x3xx = []
    dx, dy = [0, 0, 1, 1, 1, 2, 2, 2], [1, 2, 0, 1, 2, 0, 1, 2]
    for x in range(9):
        for y in range(9):
            rere = []
            if x % 3 == 0 and y % 3 == 0:
                rere.append(x3x[x][y])
                for k in range(8):
                    nx = x + dx[k]; ny = y + dy[k]
                    rere.append(x3x[nx][ny])
            if len(rere) == 9:
                x3xx.append(rere)
    return x3xx
def real(matrix):
    for i in matrix:
        if i.count(0) == 1:
            seti = set(i)
            rere = result - seti
            temp = i.index(0); temp2 = i.remove(0); i.insert(temp, *rere)
    mat = low(matrix)
    for i in mat:
        if i.count(0) == 1:
            seti = set(i)
            rere = result - seti
            temp = i.index(0); temp2 = i.remove(0); i.insert(temp, *rere)
    tam = low(mat)
    tata = x3x(tam)
    for i in tata:
        if i.count(0) == 1:
            seti = set(i)
            rere = result - seti
            temp = i.index(0); temp2 = i.remove(0); i.insert(temp, *rere)
    real = x3x(tata)
    return real
result = {1, 2, 3, 4, 5, 6, 7, 8, 9}
matrix = [list(map(int, input().rstrip().split())) for _ in range(9)]
rere = real(matrix)
for i in rere:
    if i.count(0) > 0:
        qwqw = real(rere)
        for x in qwqw:
            print(*x)
        break
else:
    for j in rere:
        print(*j)