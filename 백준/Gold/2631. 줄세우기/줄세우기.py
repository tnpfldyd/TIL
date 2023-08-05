import sys, bisect
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    tall = int(input())
    if not stack:
        stack.append(tall)
    else:
        if stack[-1] < tall:
            stack.append(tall)
        else:
            idx = bisect.bisect_left(stack, tall)
            stack[idx] = tall
print(N - len(stack))