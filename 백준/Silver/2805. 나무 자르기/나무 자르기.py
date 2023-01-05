N, M = map(int, input().split())
wood_list = list(map(int, input().split()))
left, right = 0, max(wood_list)
result = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in wood_list:
        temp = i - mid
        if temp > 0:
            cnt += temp
    if cnt < M:
        right = mid - 1
        result = right
    else:
        left = mid + 1
print(result)