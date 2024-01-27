N = int(input())
numbers = list(map(int, input().split()))
cnt = 0

while True:
    flag = True
    for i in range(N):
        if numbers[i] % 2:
            numbers[i] -= 1
            cnt += 1
        if numbers[i]:
            flag = False
    if flag:
        break
    for i in range(N):
        numbers[i] //= 2
    cnt += 1

print(cnt)