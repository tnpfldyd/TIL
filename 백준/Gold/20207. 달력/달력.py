import sys
input = sys.stdin.readline
N = int(input())
calendar = [0] * 367
for _ in range(N):
    s, e = map(int, input().split())
    for i in range(s, e + 1):
        calendar[i] += 1

row = col = result = 0

for i in range(1, 367):
    if calendar[i]:
        row = max(row, calendar[i])
        col += 1
    else:
        result += row * col
        row = col = 0
print(result)