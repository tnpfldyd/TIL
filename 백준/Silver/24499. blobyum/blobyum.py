import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

A = A + A

current_sum = sum(A[:K])
max_sum = current_sum

for i in range(K, N + K):
    current_sum += A[i]
    current_sum -= A[i - K]
    max_sum = max(max_sum, current_sum)

print(max_sum)