import sys
input = sys.stdin.readline

N = int(input())
knots = []
for _ in range(N):
    a, b = map(int, input().split())
    knots.append((a, a + b))
knots.sort()

left = 0
right = int(1e10)
result = 0

def check(distance):
    cur = knots[0][0]
    for i in range(1, N):
        if cur + distance > knots[i][1]:
            return False
        if cur + distance > knots[i][0]:
            cur += distance
        else:
            cur = knots[i][0]
    return True

while left <= right:
    mid = (left + right) // 2
    if check(mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)