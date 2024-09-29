from collections import deque
import sys
input = sys.stdin.readline

length, num_lights, target_count = map(int, input().split())
light_positions = list(map(int, input().split()))

visited = set()
queue = deque()
brightness = dict()
for position in light_positions:
    visited.add(position)
    brightness[position] = 0
    queue.append(position)

processed_count = 0
while queue:
    current_position = queue.popleft()
    processed_count += 1
    if current_position - 1 >= 0 and current_position - 1 not in visited:
        brightness[current_position - 1] = brightness[current_position] + 1
        visited.add(current_position - 1)
        queue.append(current_position - 1)
    if current_position + 1 <= length and current_position + 1 not in visited:
        brightness[current_position + 1] = brightness[current_position] + 1
        visited.add(current_position + 1)
        queue.append(current_position + 1)
    if processed_count == target_count:
        break

sorted_brightness = sorted(brightness.items(), key=lambda x:x[1])
for i in range(target_count):
    print(sorted_brightness[i][1])