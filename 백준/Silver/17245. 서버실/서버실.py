import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

total = sum(map(sum, grid))
target = (total + 1) // 2

def can_operate(t):
    s = 0
    for row in grid:
        for h in row:
            s += h if h < t else t
            if s >= target:
                return True
    return False

left, right = 0, 10_000_000
while left < right:
    mid = (left + right) // 2
    if can_operate(mid):
        right = mid
    else:
        left = mid + 1

print(left)