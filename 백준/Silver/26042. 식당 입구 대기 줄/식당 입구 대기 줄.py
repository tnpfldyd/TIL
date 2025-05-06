import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()
max_count = 0
min_back_id = float('inf')

for _ in range(n):
    parts = input().split()
    if parts[0] == '1':
        student_id = int(parts[1])
        queue.append(student_id)
        if len(queue) > max_count or (len(queue) == max_count and queue[-1] < min_back_id):
            max_count = len(queue)
            min_back_id = queue[-1]
    else:
        queue.popleft()

print(max_count, min_back_id)