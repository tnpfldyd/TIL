import sys
input = sys.stdin.readline

N = int(input())
light_arrangement = list(input().strip())
color_change = {'R': 'G', 'G': 'B', 'B': 'R'}

def change_light(index, arrangement):
    arrangement[index], arrangement[index + 1], arrangement[index + 2] = color_change[arrangement[index]], color_change[arrangement[index + 1]], color_change[arrangement[index + 2]]
    return arrangement

def solve(arrangement):
    move_count = 0

    for i in range(1, N - 2):
        while arrangement[0] != arrangement[i]:
            move_count += 1
            arrangement = change_light(i, arrangement)

    if arrangement[0] == arrangement[-1] == arrangement[-2]:
        return move_count
    return float('inf')

min_moves = float('inf')

for i in range(3):
    min_moves = min(min_moves, solve(light_arrangement.copy()) + i)

    light_arrangement = change_light(0, light_arrangement)

if min_moves == float('inf'):
    min_moves = -1
print(min_moves)
