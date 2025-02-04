n = int(input())
a = list(map(int, input().split()))
result = []
min_val = a[0]
max_diff = 0
result.append(max_diff)
for i in range(1, n):
    current = a[i]
    if current < min_val:
        min_val = current
    current_diff = current - min_val
    if current_diff > max_diff:
        max_diff = current_diff
    result.append(max_diff)
print(' '.join(map(str, result)))