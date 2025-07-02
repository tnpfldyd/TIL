import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))

left = max(lectures)
right = sum(lectures)
result = right

def count_disks(size):
    count = 1
    total = 0
    for lecture in lectures:
        if total + lecture > size:
            count += 1
            total = 0
        total += lecture
    return count

while left <= right:
    mid = (left + right) // 2
    needed = count_disks(mid)
    if needed <= m:
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)