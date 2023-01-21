from collections import deque
N, K = map(int, input().split())
stack = deque()
result = []
for i in range(1, N + 1):
    stack.append(i)
print('<', end='')
while stack:
    for i in range(K - 1):
        stack.append(stack.popleft())
    result.append(stack.popleft())
    print(result[-1], end='')
    if stack:
        print(', ', end='')
    else:
        print('>')