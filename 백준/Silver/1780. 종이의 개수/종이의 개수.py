import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
count_minus1 = 0
count_zero = 0
count_plus1 = 0

def divide(x, y, size):
    global count_minus1, count_zero, count_plus1
    first = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first:
                m = size // 3
                for dx in range(3):
                    for dy in range(3):
                        divide(x + dx * m, y + dy * m, m)
                return
    if first == -1:
        count_minus1 += 1
    elif first == 0:
        count_zero += 1
    else:
        count_plus1 += 1

divide(0, 0, n)
print(count_minus1)
print(count_zero)
print(count_plus1)