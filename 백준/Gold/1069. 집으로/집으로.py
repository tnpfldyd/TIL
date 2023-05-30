x, y, d, t = map(int, input().split())
dist = (x * x + y * y) ** 0.5
jump = dist // d
remain = dist - jump * d

ans = min(dist, remain + jump * t)
ans = min(ans, (jump + 1) * d - dist + (jump + 1) * t)

if jump:
    ans = min(ans, (jump + 1) * t)
else:
    if dist < d:
        ans = min(ans, t * 2.0)

print('{:.9f}'.format(ans))