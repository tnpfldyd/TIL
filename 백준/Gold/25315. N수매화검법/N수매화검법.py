import sys
input = sys.stdin.readline

def calculate_orientation(x1, y1, x2, y2, x3, y3):
    result = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    if result == 0:
        return 0
    elif result < 0:
        return -1
    elif result > 0:
        return 1

def check_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    orientation1 = calculate_orientation(x1, y1, x2, y2, x3, y3) * calculate_orientation(x1, y1, x2, y2, x4, y4)
    orientation2 = calculate_orientation(x3, y3, x4, y4, x1, y1) * calculate_orientation(x3, y3, x4, y4, x2, y2)

    if orientation1 == 0 and orientation2 == 0:
        if x1 + y1 > x2 + y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        if x3 + y3 > x4 + y4:
            x3, y3, x4, y4 = x4, y4, x3, y3

        return x1 + y1 <= x4 + y4 and x3 + y3 <= x2 + y2

    return orientation1 <= 0 and orientation2 <= 0

num_segments = int(input())
segment_data = []

for _ in range(num_segments):
    x1, y1, x2, y2, weight = map(int, input().split())
    segment_data.append((weight, x1, y1, x2, y2))

segment_data.sort()
total_weight = 0

for i in range(num_segments):
    intersection_count = 1

    for j in range(i + 1, num_segments):
        seg1_x1, seg1_y1, seg1_x2, seg1_y2 = segment_data[i][1], segment_data[i][2], segment_data[i][3], segment_data[i][4]
        seg2_x1, seg2_y1, seg2_x2, seg2_y2 = segment_data[j][1], segment_data[j][2], segment_data[j][3], segment_data[j][4]

        if check_intersection(seg1_x1, seg1_y1, seg1_x2, seg1_y2, seg2_x1, seg2_y1, seg2_x2, seg2_y2):
            intersection_count += 1

    total_weight += segment_data[i][0] * intersection_count

print(total_weight)