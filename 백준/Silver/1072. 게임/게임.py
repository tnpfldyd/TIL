import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = Y * 100 // X
if Z >= 99:
    print(-1)
    sys.exit()

left, right = 1, 10**9
ans = 0
while left <= right:
    mid = (left + right) // 2
    if (Y + mid) * 100 // (X + mid) > Z:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)