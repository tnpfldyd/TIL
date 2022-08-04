import sys

sys.stdin = open("1974input.txt", "r")
T = int(input())
for i in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    row = []
    for x in range(9):
        row_ = set()
        for y in range(9):
            row_.add(matrix[x][y])
        row.append(row_)
    col = []
    for x in range(9):
        col_ = set()
        for y in range(9):
            col_.add(matrix[y][x])
        col.append(col_)
    box = []
    q = 0
    for _ in range(3):        
        j = 0
        for __ in range(3):
            box_ = set()
            for x in range(q, q+3):
                for y in range(j, j+3):
                    box_.add(matrix[x][y])
            box.append(box_)
            j += 3
        q += 3
    if sum(map(sum, row)) + sum(map(sum, col)) + sum(map(sum, box)) == 1215:
        print(f'#{i}', 1)
    else:
        print(f'#{i}', 0)