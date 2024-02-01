def can_ride(x):
    cnt = 1
    start = 0
    for i in range(1, N):
        if i - start < C and numbers[i] <= numbers[start] + x:
            continue
        cnt += 1
        start = i
    return cnt <= M

N, M, C = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

left = 0
right = 10 ** 9

while left <= right:
    mid = (left + right) // 2
    if can_ride(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)