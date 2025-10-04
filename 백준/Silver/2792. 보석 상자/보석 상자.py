import sys
input = sys.stdin.readline

N, M = map(int, input().split())
jewels = [int(input()) for _ in range(M)]

def can_distribute(max_jealousy):
    students_needed = 0
    for jewel_count in jewels:
        students_needed += (jewel_count + max_jealousy - 1) // max_jealousy
        if students_needed > N:
            return False
    return True

left, right = 1, max(jewels)
result = right

while left <= right:
    mid = (left + right) // 2
    if can_distribute(mid):
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)