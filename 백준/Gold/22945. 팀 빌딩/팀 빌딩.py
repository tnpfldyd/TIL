N = int(input())
numbers = list(map(int, input().split()))
l, r = 0, N - 1
answer = 0
while l <= r:
    min_num = min(numbers[l], numbers[r])
    answer = max(answer, (r - l - 1) * min_num)
    if numbers[l] < numbers[r]:
        l += 1
    else:
        r -= 1
print(answer)