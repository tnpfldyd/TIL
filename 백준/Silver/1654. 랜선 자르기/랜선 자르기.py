import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lines = []
for _ in range(N):
    lines.append(int(input()))

left, right = 1, max(lines)
answer = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for line in lines:
        cnt += line // mid
    if cnt < M:
        right = mid - 1
    else:
        left = mid + 1
print(right)