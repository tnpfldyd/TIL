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

arr_cnt = sorted(arr_cnt.items(), key=lambda x : -x[1])

for k, v in arr_cnt:
    zero_cnt = k.count('0')
    if zero_cnt <= K and zero_cnt % 2 == K % 2:
        answer = v
        break

print(answer)