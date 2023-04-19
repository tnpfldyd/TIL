import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
points.sort()

def get_dist(x, y):
    x1, y1 = points[x]
    x2, y2 = points[y]
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def BinarySearch(left, right):
    if left == right:
        return INF
    if left + 1 >= right:
        return get_dist(left, right)
    mid = (left + right) // 2
    min_dist = min(get_dist(left, right), BinarySearch(left, mid), BinarySearch(mid + 1, right))
    area = []
    mid_x = points[mid][0]

    for i in range(mid, left - 1, -1):
        x = points[i][0]
        dist = (x - mid_x) ** 2
        if min_dist <= dist:
            break
        area.append((points[i]))

    for i in range(mid + 1, right + 1):
        x = points[i][0]
        dist = (x - mid_x) ** 2
        if min_dist <= dist:
            break
        area.append((points[i]))
    if not area:
        return min_dist
    area = sorted(area, key=lambda x : x[1])
    for i in range(len(area)):
        x1, y1 = area[i]
        for j in range(i + 1, len(area)):
            x2, y2 = area[j]
            dist_x = (x1 - x2) ** 2
            dist_y = (y1 - y2) ** 2
            if min_dist <= dist_x:
                continue
            if min_dist <= dist_y:
                break
            min_dist = min(min_dist, dist_x + dist_y)
    
    return min_dist

result = BinarySearch(0, N - 1)

print(result)