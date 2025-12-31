n = int(input())
numbers = list(map(int, input().split()))
target = int(input())

left, right = 0, 0
current_sum = 0
count = 0

while left < n:
    while right < n and current_sum + numbers[right] <= target:
        current_sum += numbers[right]
        right += 1

    count += n - right
    current_sum -= numbers[left]
    left += 1
    
print(count)