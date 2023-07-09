N = int(input())
numbers = sorted(list(map(int, input().split())))
result = float('inf')
l, r = 0, N - 1
a, b = 0, 0
while l < r:
    cur = numbers[l] + numbers[r]
    if result > abs(cur):
        result = abs(cur)
        a, b = l, r
        if not cur:
            break
    if cur < 0:
        l += 1
    else:
        r -= 1
print(numbers[a], numbers[b])