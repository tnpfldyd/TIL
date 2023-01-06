import sys
input = sys.stdin.readline
N, M = map(int, input().split())
adress = [int(input()) for _ in range(N)]
adress.sort()
left, right = 0, adress[-1] - adress[0]
answer = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 1
    house = adress[0]
    for i in range(1, len(adress)):
        if adress[i] - house >= mid:
            cnt += 1
            house = adress[i]
    if cnt < M:
        right = mid - 1
    else:
        left = mid + 1
        answer = max(answer, mid)
print(answer)