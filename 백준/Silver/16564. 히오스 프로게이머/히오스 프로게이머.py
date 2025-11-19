import sys
input = sys.stdin.readline

N, K = map(int, input().split())
X = [int(input()) for _ in range(N)]

lo = min(X)
hi = max(X) + K
ans = lo

while lo <= hi:
    mid = (lo + hi) // 2
    need = 0
    for x in X:
        if x < mid:
            need += mid - x
            if need > K:
                break
    if need <= K:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)