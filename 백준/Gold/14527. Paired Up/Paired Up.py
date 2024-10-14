import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
A.sort(key=lambda x:x[1])
l, r = 0, N - 1
ans = 0
while l <= r:
    pairs = min(A[l][0], A[r][0])
    if l == r: pairs //= 2
    cnt = A[l][1] + A[r][1]
    ans = max(ans, cnt)
    A[l][0] -= pairs
    A[r][0] -= pairs
    if A[l][0] == 0: l += 1
    if A[r][0] == 0: r -= 1
print(ans)