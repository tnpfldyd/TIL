import sys

input = sys.stdin.readline
road_length = int(input())
max_range, damage_per_meter = map(int, input().split())
mine_count = int(input())
zombies = [0] + [int(input()) for _ in range(road_length)]

def can_defend(mine_count):
    accumulated_damage = [0]

    for position in range(1, road_length + 1):
        start_range = max(0, position - max_range)
        current_damage = accumulated_damage[position - 1] - accumulated_damage[start_range]

        if zombies[position] <= current_damage + damage_per_meter:
            accumulated_damage.append(accumulated_damage[position - 1] + damage_per_meter)
        else:
            if mine_count > 0:
                mine_count -= 1
                accumulated_damage.append(accumulated_damage[position - 1])
            else:
                return "NO"

    return "YES"

print(can_defend(mine_count))