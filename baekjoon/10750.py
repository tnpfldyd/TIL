S, T = input(), list(input())
stack = []
for s in S:
    stack.append(s)
    if stack[-len(T):] == T:
        for _ in range(len(T)):
            stack.pop()

print(''.join(stack))