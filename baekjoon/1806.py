N, S = map(int, input().split())
numbers = list(map(int, input().split())) + [0]
left = rigth = 0
total = numbers[0]
answer = float('inf')
while left <= rigth and rigth < N:
    if total < S:
        rigth += 1
        total += numbers[rigth]
    else:
        answer = min(answer, rigth - left + 1)
        total -= numbers[left]
        left += 1
print(answer if answer != float('inf') else 0)