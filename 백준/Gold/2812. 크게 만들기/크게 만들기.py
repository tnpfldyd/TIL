N, K = map(int, input().split())
number = input()

stack = []
for i in range(N):
    while stack and K and int(stack[-1]) < int(number[i]):
        stack.pop()
        K -= 1
    stack.append(number[i])
if K:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))