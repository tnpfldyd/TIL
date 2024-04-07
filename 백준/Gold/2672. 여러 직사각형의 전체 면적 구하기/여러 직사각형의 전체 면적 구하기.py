import sys
input = sys.stdin.readline

N = int(input())
rectangles = []
for _ in range(N):
    x, y, w, h = map(float, input().split())
    x, y, w, h = int(x * 10), int(y * 10), int(w * 10), int(h * 10)
    rectangles.append((x, y, y + h, 1))
    rectangles.append((x + w, y, y + h, -1))

rectangles.sort()

rectangleCounts = [0] * 20001
answer = 0
last_x = 0
for x, y1, y2, chk in rectangles:
    cnt = sum(1 for count in rectangleCounts if count > 0)
    answer += cnt * (x - last_x)
    for i in range(y1 + 1, y2 + 1):
        rectangleCounts[i] += chk
    last_x = x

print(answer // 100 if answer % 100 == 0 else '{:.2f}'.format(answer / 100))