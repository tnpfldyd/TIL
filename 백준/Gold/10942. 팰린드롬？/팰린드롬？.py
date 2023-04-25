import sys

input = sys.stdin.readline

N = int(input())
numbers = [0] + list(map(int, input().split()))

check = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    if i != N and numbers[i] == numbers[i + 1]:
        check[i][i + 1] = 1
    check[i][i] = 1

for i in range(N - 1, 0, -1):
    for j in range(i + 2, N + 1):
        if numbers[i] == numbers[j] and check[i + 1][j - 1]:
            check[i][j] = 1

M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(check[s][e])