n = int(input())
left = 1
right = 1
sum_val = 1
count = 0

while left <= n:
    if sum_val == n:
        count += 1
        sum_val -= left
        left += 1
    elif sum_val < n:
        right += 1
        sum_val += right
    else:
        sum_val -= left
        left += 1

print(count)