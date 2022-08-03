import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
T = int(input())
for t in range(T):
    cnt = 0
    i, j, x, y =map(int, input().split())
    for q in range(i-1, x):
        for p in range(j-1, y):
            cnt += matrix[q][p]
    print(cnt)