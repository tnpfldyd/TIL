ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())

def distance(x1, y1, z1, x2, y2, z2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

min_length = 1e9
len_start_c = distance(ax, ay, az, cx, cy, cz)
len_end_c = distance(bx, by, bz, cx, cy, cz)

while True:
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    mz = (az + bz) / 2
    len_mid_c = distance(mx, my, mz, cx, cy, cz)
    
    if abs(min_length - len_mid_c) <= 1e-6:
        print('{:.10f}'.format(len_mid_c))
        break
    
    min_length = min(len_mid_c, min_length)
    
    if len_start_c < len_end_c:
        bx, by, bz = mx, my, mz
        len_end_c = len_mid_c
    else:
        ax, ay, az = mx, my, mz
        len_start_c = len_mid_c
