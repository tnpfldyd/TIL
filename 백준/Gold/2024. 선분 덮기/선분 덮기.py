from collections import deque
import sys

input = sys.stdin.readline

TARGET = int(input())

lines = []
while True:
    start, end = map(int, input().split())
    if start == end == 0:
        break
    if start == end or (start < 0 and end <= 0):
        continue
    lines.append((start, end))

sorted_lines = deque(sorted(lines))

def cover_line():
    current_end = 0
    used_lines = 0

    while sorted_lines:
        candidates = []
        current_line = sorted_lines.popleft()
        
        if current_line[0] <= current_end:
            candidates.append(current_line[1])
        
        if current_end < current_line[0]:
            return 0

        while sorted_lines and sorted_lines[0][0] <= current_end:
            candidates.append(sorted_lines.popleft()[1])

        current_end = max(candidates)
        used_lines += 1

        if current_end >= TARGET:
            return used_lines

    return 0

print(cover_line())