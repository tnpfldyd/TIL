import bisect
N = int(input())
numbers = list(map(int, input().split()))

stack = []
for number in reversed(numbers):
    if not stack:
        stack.append(number)
    else:
        if stack[-1] < number:
            stack.append(number)
        else:
            idx = bisect.bisect_left(stack, number)
            stack[idx] = number
print(len(stack))