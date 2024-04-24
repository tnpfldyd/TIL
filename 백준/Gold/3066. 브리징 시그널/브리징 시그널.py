import sys, bisect
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())

    stack = []
    for _ in range(N):
        num = int(input())
        if not stack or stack[-1] < num:
            stack.append(num)
        else:
            idx = bisect.bisect_left(stack, num)
            stack[idx] = num

    print(len(stack))