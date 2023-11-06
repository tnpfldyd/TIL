import sys
input = sys.stdin.readline

N = int(input())

lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort()

answer = 0
left = lines[0][0]
right = lines[0][1]

for i in range(1, N):
    start, end = lines[i]
    if start <= right:
        right = max(right, end)
    else:
        answer += right - left
        left = start
        right = end
answer += right - left
print(answer)