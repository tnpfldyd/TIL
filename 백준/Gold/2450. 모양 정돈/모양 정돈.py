from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
shapes = list(map(int, input().split()))
shape_count = [0] * 4
min_swaps = float('inf')

for shape in shapes:
    shape_count[shape] += 1

for perm in permutations([1, 2, 3]):
    area_count = [[0] * 4 for _ in range(4)]

    current_index = 0
    for i in range(3):
        count_in_section = shape_count[perm[i]]
        for j in range(current_index, current_index + count_in_section):
            area_count[perm[i]][shapes[j]] += 1
        current_index += count_in_section

    swaps_needed = area_count[1][2] + area_count[1][3]
    swaps_needed += max(area_count[2][3], area_count[3][2])

    min_swaps = min(min_swaps, swaps_needed)

print(min_swaps)