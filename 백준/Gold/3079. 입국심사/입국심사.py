import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())

times = sorted([int(input()) for _ in range(N)])

left, right = 1, times[0] * M

answer = 0

while left <= right:
    result = 0
    mid = (left + right) // 2
    for i in range(N):
        result += mid // times[i]
    if result < M:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)