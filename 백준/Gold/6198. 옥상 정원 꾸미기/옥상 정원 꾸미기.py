import sys
input = sys.stdin.readline

stack = []
N = int(input())
answer = 0
for _ in range(N):
    height = int(input())
    while stack and stack[-1] <= height:
        stack.pop()
    answer += len(stack)
    stack.append(height)
print(answer)