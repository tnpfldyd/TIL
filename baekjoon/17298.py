N = int(input())
numbers = list(map(int, input().split()))
stack = []
answer = [0] * N

for i in range(N-1, -1, -1):
    while stack and stack[-1] <= numbers[i]:
        stack.pop()
    if not stack:
        answer[i] = -1
    else:
        answer[i] = stack[-1]
    stack.append(numbers[i])

print(*answer)