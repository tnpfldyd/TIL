N, K = int(input()), int(input())
low, high = 1, K

while low < high:
    mid = (low + high) // 2
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(mid // i, N)
    if K <= cnt:
        high = mid
    else:
        low = mid + 1

print(low)