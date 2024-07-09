import math
x1, y1, r1, x2, y2, r2 = map(float, input().split())

def calc_inter_area(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    r1_sq = r1 * r1
    r2_sq = r2 * r2
    
    if d > r1 + r2:
        return 0
    elif d <= abs(r1 - r2) and r1 < r2:
        return math.pi * r1_sq
    elif d <= abs(r1 - r2) and r1 >= r2:
        return math.pi * r2_sq
    else:
        phi = (math.acos((r1_sq + d**2 - r2_sq) / (2 * r1 * d))) * 2
        theta = (math.acos((r2_sq + d**2 - r1_sq) / (2 * r2 * d))) * 2
        area1 = 0.5 * r2_sq * (theta - math.sin(theta))
        area2 = 0.5 * r1_sq * (phi - math.sin(phi))
        return area1 + area2

result = float(round(1000 * calc_inter_area(x1, y1, r1, x2, y2, r2)) / 1000)
print('%.3f' % result)
