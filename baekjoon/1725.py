import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]

maxSize = 0
stack = []
for i in range(N):
    cur = i
    while stack and stack[-1][0] >= numbers[i]:
        height, cur = stack.pop()
        maxSize = max(maxSize, (i - cur) * height)
    stack.append((numbers[i], cur))
for height, index in stack:
    maxSize = max(maxSize, (N - index) * height)
print(maxSize)