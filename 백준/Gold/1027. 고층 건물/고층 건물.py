def get_dist(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

N = int(input())

buildings = list(map(int, input().split()))

result = 0
for s, y1 in enumerate(buildings):
    x1 = s + 1
    cur = None
    right = 0
    for e in range(s + 1, N):
        x2 = e + 1
        y2 = buildings[e]
        dist = get_dist(x1, y1, x2, y2)
        if cur is None or cur < dist:
            cur = dist
            right += 1

    cur = None
    left = 0
    for e in range(s - 1, -1, -1):
        x2 = e + 1
        y2 = buildings[e]
        dist = get_dist(x1, y1, x2, y2)
        
        if cur is None or cur > dist:
            cur = dist
            left += 1

    if left + right > result: 
        result = left + right

print(result)