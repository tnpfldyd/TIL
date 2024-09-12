import sys
from collections import defaultdict

input = sys.stdin.readline
num_ingredients, max_bacteria, max_removals = map(int, input().split())
ingredients_info = defaultdict(list)

for _ in range(num_ingredients):
    spoilage_rate, expiry_day, is_removable = map(int, input().split())
    ingredients_info[is_removable].append((spoilage_rate, expiry_day))

def calculate_bacteria(day, removals_left):
    total_bacteria = 0

    for spoilage_rate, expiry_day in ingredients_info[0]:
        total_bacteria += spoilage_rate * max(1, day - expiry_day)

    ingredients_info[1].sort(key=lambda item: -item[0] * max(1, day - item[1]))
    
    for index in range(removals_left, len(ingredients_info[1])):
        spoilage_rate, expiry_day = ingredients_info[1][index]
        total_bacteria += spoilage_rate * max(1, day - expiry_day)
    
    return total_bacteria

max_days = 0
left, right = 0, int(2e9)

while left <= right:
    mid = (left + right) // 2
    total_bacteria = calculate_bacteria(mid, max_removals)
    
    if total_bacteria <= max_bacteria:
        max_days = mid
        left = mid + 1
    else:
        right = mid - 1

print(max_days)