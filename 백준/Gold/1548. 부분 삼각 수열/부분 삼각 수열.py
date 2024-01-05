N = int(input())
numbers = sorted(list(map(int, input().split())))
result = 2
for left in range(N - 1):
    for right in range(N - 1, -1, -1):
        if left + 1 == right:
            break
        if numbers[left] + numbers[left + 1] > numbers[right]:
            result = max(result, right - left + 1)
            break
print(min(result, N))