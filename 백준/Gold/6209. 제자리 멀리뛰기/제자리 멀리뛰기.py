import sys
input = sys.stdin.readline

d, n, m = map(int, input().split())
islands = sorted([int(input()) for _ in range(n)])
left, right = 0, d
answer = 0
while left <= right:
    mid = (left + right) // 2
    count = 0
    prev = 0
    for island in islands:
        if island - prev < mid:
            count += 1
        else:
            prev = island
    
    if count > m:
        right = mid - 1
    else:
        left = mid + 1
        answer = mid
print(answer)