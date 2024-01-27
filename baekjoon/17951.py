N, K = map(int, input().split())
score = list(map(int, input().split()))

left, right = 0, sum(score)

while left <= right:
    mid = (left + right) // 2
    temp = 0
    cnt = 0
    for i in range(N):
        temp += score[i]
        if temp >= mid:
            cnt += 1
            temp = 0
        if cnt == K:
            left = mid + 1
            break
    else:
        right = mid - 1
        
print(right)