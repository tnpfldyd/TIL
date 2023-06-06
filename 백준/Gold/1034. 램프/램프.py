from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
arr_cnt = defaultdict(int)
for _ in range(N):
    arr = input().strip()
    arr_cnt[arr] += 1
    matrix.append(arr)
K = int(input())

answer = 0

for i in range(N):
    zero_cnt = 0
    for j in range(M):
        if not int(matrix[i][j]):
            zero_cnt += 1
    if zero_cnt <= K and zero_cnt % 2 == K % 2:
        answer = max(answer, arr_cnt[matrix[i]])

print(answer)