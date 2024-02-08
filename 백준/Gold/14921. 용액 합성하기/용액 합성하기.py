
N = int(input())
numbers = list(map(int, input().split()))

left, right = 0, N - 1
result = numbers[left] + numbers[right]
while left < right:
    temp = numbers[left] + numbers[right]
    if abs(temp) < abs(result):
        result = temp
    if temp > 0:
        right -= 1
    else:
        left += 1

print(result)