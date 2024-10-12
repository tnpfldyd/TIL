import sys

input = sys.stdin.readline

N = int(input())
stack = []
total_count = 0
max_num = 0

for _ in range(N):
    current = int(input())
    max_num = max(max_num, current)
    
    if not stack:
        stack.append(current)
    else:
        if stack[-1] < current:
            total_count += current - stack[-1]
            stack.pop()
            stack.append(current)
        elif stack[-1] > current:
            stack.pop()
            stack.append(current)

while stack:
    num = stack.pop()
    total_count += max_num - num

print(total_count)