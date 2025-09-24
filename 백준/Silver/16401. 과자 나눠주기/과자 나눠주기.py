import sys
input = sys.stdin.readline

M, N = map(int, input().split())
cookies = list(map(int, input().split()))

def can_distribute(length):
    total = 0
    for cookie in cookies:
        total += cookie // length
    return total >= M

left, right = 1, max(cookies)
result = 0

while left <= right:
    mid = (left + right) // 2
    if can_distribute(mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)