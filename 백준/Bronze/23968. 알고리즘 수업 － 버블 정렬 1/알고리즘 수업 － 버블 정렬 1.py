import sys
input = sys.stdin.readline

def kth_bubble_swap(N, K, A):
    cnt = 0
    for last in range(N-1, 0, -1):
        for i in range(last):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                cnt += 1
                if cnt == K:
                    return sorted([A[i], A[i+1]])
    return [-1]

N, K = map(int, input().split())
A = list(map(int, input().split()))

result = kth_bubble_swap(N, K, A)

if result[0] == -1:
    print(-1)
else:
    print(*result)