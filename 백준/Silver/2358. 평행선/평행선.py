import sys
input = sys.stdin.readline

n = int(input())
x_count = {}
y_count = {}

for _ in range(n):
    x, y = map(int, input().split())
    x_count[x] = x_count.get(x, 0) + 1
    y_count[y] = y_count.get(y, 0) + 1

result = sum(1 for v in x_count.values() if v >= 2) + sum(1 for v in y_count.values() if v >= 2)
print(result)