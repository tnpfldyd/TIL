from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A_sum = defaultdict(int)
B_sum = defaultdict(int)
for i in range(n):
    acc = 0
    for j in range(i, n):
        acc += A[j]
        A_sum[acc] += 1
for i in range(m):
    acc = 0
    for j in range(i, m):
        acc += B[j]
        B_sum[acc] += 1

cnt = 0
for a_sum in A_sum:
    if T - a_sum in B_sum:
        cnt += A_sum[a_sum] * B_sum[T-a_sum]
print(cnt)