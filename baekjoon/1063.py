command = {'R':(0, 1), 'L':(0, -1), 'B':(1, 0), 'T':(-1, 0), 'RT':(-1, 1), 'LT':(-1, -1), 'RB':(1, 1), 'LB':(1, -1)}
k, s, n = input().split()
kx, ky = 8 - int(k[1]), ord(k[0]) - 65
sx, sy = 8 - int(s[1]), ord(s[0]) - 65
matrix = [[0] * 8 for _ in range(8)]
matrix[kx][ky] = 1
matrix[sx][sy] = 2
for i in range(int(n)):
    com = input()
    dx, dy = command.get(com)
    if sx == kx + dx and sy == ky + dy:
        if 0 <= sx + dx < 8 and 0 <= sy + dy < 8:
            matrix[kx][ky] = 0
            kx += dx; ky += dy; sx += dx; sy += dy
            matrix[kx][ky], matrix[sx][sy] = 1, 2
    else:
        if 0 <= kx + dx < 8 and 0<= ky + dy < 8:
            matrix[kx][ky] = 0
            kx += dx; ky += dy
            matrix[kx][ky] = 1
result = []
result1 = []
for i in range(8):
    for j in range(8):
        if matrix[i][j] == 1:
            result.append((i, j))
        elif matrix[i][j] == 2:
            result1.append((i, j))
origin = chr(result[0][1] + 65) + str(abs(result[0][0] - 8))
origin1 = chr(result1[0][1] + 65) + str(abs(result1[0][0] - 8))
print(origin)
print(origin1)
# 풀고나서 코드리뷰 하고 보니 굳이 구현할 필요 없었던 문제인데.. 라는 생각에 살짝 현타가..
