import sys
input = sys.stdin.readline

N = int(input())
points = []
for i in range(N):
    x, r = map(int, input().split())
    points.append((x - r, i))
    points.append((x + r, i))

points.sort()

stack = []
for _, flag in points:
    if stack and stack[-1] == flag:
        stack.pop()
    else:
        stack.append(flag)

print("NO" if stack else "YES")