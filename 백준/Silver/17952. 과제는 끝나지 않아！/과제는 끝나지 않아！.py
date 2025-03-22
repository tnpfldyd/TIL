import sys
input = sys.stdin.readline

N = int(input())
stack = []
current = None
total_score = 0

for _ in range(N):
    line = list(map(int, input().split()))
    if line[0] == 1:
        A, T = line[1], line[2]
        if current:
            stack.append(current)
        current = [A, T]
    if current:
        current[1] -= 1
        if current[1] == 0:
            total_score += current[0]
            current = stack.pop() if stack else None

print(total_score)