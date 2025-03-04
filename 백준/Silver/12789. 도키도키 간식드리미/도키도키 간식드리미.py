from collections import deque

N = int(input())
line = deque(map(int, input().split()))

stack = []
target = 1

while line or stack:
    if line and line[0] == target:
        line.popleft()
        target += 1
    elif stack and stack[-1] == target:
        stack.pop()
        target += 1
    elif line:
        stack.append(line.popleft())
    else:
        break

if target == N + 1:
    print("Nice")
else:
    print("Sad")