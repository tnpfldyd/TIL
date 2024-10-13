N, K = map(int, input().split())
ans = [0] * (N + 1)
start, end = 1, N

for i in range(1, N + 1):
    if K >= N - i:
        K -= (N - i)
        ans[i] = end
        end -= 1
    else:
        ans[i] = start
        start += 1

if K != 0 or start <= end:
    print(-1)
else:
    print(*ans[1:])
