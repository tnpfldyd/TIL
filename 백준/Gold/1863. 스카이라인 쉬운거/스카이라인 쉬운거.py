import sys
input = sys.stdin.readline

def solve(x, y):
    global cnt
    while stack and y < stack[-1][1]:
        cnt += 1
        stack.pop()
    if not stack or stack[-1][1] != y:
        stack.append((x, y))

N = int(input())
stack = []
cnt = 0

for _ in range(N):
    x, y = map(int, input().split())
    solve(x, y)

while stack:
    if stack[-1][1] > 0:
        cnt += 1
    stack.pop()

print(cnt)