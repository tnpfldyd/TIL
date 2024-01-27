N, M = map(int, input().split())
numbers = list(map(int, input().split()))
left, right = 0, max(numbers)

result = 0

def isPossible(mid):
    cnt = 1
    minValue = maxValue = numbers[0]
    for i in range(1, N):
        cur = numbers[i]
        if cur < minValue:
            minValue = cur
        if cur > maxValue:
            maxValue = cur
        if maxValue - minValue > mid:
            cnt += 1
            minValue = maxValue = cur
    return cnt <= M

while left <= right:
    mid = (left + right) // 2
    if isPossible(mid):
        result = mid
        right = mid - 1
    else:
        left = mid + 1
    
print(result)