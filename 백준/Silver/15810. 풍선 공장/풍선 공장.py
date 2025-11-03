import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = list(map(int, input().split()))

def can_make(time):
    total = 0
    for t in times:
        total += time // t
        if total >= M:
            return True
    return total >= M

left, right = 1, min(times) * M

answer = right
while left <= right:
    mid = (left + right) // 2
    
    if can_make(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)