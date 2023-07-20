import sys
input = sys.stdin.readline
M, N, L = map(int, input().split())
mList = sorted(list(map(int, input().strip().split())))
coordinate = [tuple(map(int, input().split())) for _ in range(N)]
result = 0

for i in range(N):
    l, r = 0, M - 1
    x, y = coordinate[i]
    while l <= r:
        mid = (l + r) // 2
        cal = abs(mList[mid] - x) + y
        if cal <= L:
            result += 1
            break
        if x >= mList[mid]:
            l = mid + 1
        else:
            r = mid - 1
print(result)