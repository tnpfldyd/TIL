N, M, L = map(int, input().split())
locations = [0] + list(map(int, input().split())) + [L]
locations.sort()

l, r = 1, L-1
result = 0
while l <= r:
    mid = (l + r) // 2
    val = 0
    for i in range(1, N + 2):
        diff = locations[i] - locations[i - 1]
        val += diff // mid
        if not diff % mid:
            val -= 1
    if val > M:
        l = mid + 1
    else:
        r = mid - 1
        result = mid
print(result)