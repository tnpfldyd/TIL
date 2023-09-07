X, Y, C = map(float, input().split())

l, r = 0, min(X, Y)
result = 0

def get_cal(m):
    h1 = (X ** 2 - m ** 2) ** 0.5
    h2 = (Y ** 2 - m ** 2) ** 0.5
    return (h1 * h2) / (h1 + h2)

while r - l > 0.000001:
    mid = (l + r) / 2
    if get_cal(mid) < C:
        r = mid
    else:
        l = mid
        result = mid

print(result)