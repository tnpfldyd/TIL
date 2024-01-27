import sys
input = sys.stdin.readline

N = int(input())
points = sorted([int(input()) for _ in range(N)])

target = 1
result = 0
for point in points:
    if point < target:
        continue
    result += point - target
    target += 1

print(result)