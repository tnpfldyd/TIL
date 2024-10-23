N = int(input())
A = sorted(map(int, input().split()))
h = N // 2

if N % 2 == 0:
    result = 2 * sum(A[h + 1:N]) - 2 * sum(A[:h - 1]) + A[h] - A[h - 1]
else:
    result = sum(A[h:N]) + sum(A[h + 2:N]) - 2 * sum(A[:h])
    result = max(result, 2 * sum(A[h + 1:N]) - sum(A[:h - 1]) - sum(A[:h + 1]))

print(result)
