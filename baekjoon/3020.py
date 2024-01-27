import sys
input = sys.stdin.readline

N, H = map(int, input().split())
bottom = [0] * (H + 1)
top = [0] * (H + 1)
for i in range(N // 2):
    l, r = int(input()), int(input())
    bottom[l] += 1
    top[r] += 1

for i in range(H - 1, 0, -1):
    bottom[i] += bottom[i + 1]
    top[i] += top[i + 1]

answer = 200000
cnt = 0

for i in range(1, H + 1):
    cur = bottom[i] + top[H - i + 1]
    if answer > cur:
        answer = cur
        cnt = 1
    elif answer == cur:
        cnt += 1

print(answer, cnt)