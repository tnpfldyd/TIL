import sys
INF = sys.maxsize
input = sys.stdin.readline
N, M = map(int, input().split())
result = ''
minX, minY, minVal = 0, 0, INF
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if (i + j) % 2 and row[j] < minVal:
            minVal = row[j]
            minX, minY = i, j
if N % 2:
    result += 'R' * (M - 1)
    for i in range(1, N):
        result += 'D'
        result += 'L' * (M - 1) if i % 2 else 'R' * (M - 1)
elif M % 2:
    result += 'D' * (N - 1)
    for i in range(1, M):
        result += 'R'
        result += 'U' * (N - 1) if i % 2 else 'D' * (N - 1)
else:
    past = False
    for i in range(0, N, 2):
        if minX == i or minX == i + 1:
            past = True
            flag = False
            if i:
                result += 'D'
            for j in range(M):
                if j:
                    result += 'R'
                if j != minY:
                    if flag:
                        result += 'U'
                    else:
                        result += 'D'
                    flag = not flag
        else:
            if i:
                result += 'D'
            result += 'L' * (M - 1) + 'D' + 'R' * (M - 1) if past else 'R' * (M - 1) + 'D' + 'L' * (M - 1)
print(result)