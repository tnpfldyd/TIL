# 건물 보이는거 찾기
heights = [5, 5, 5]

stack = []
answer = 0
for v in heights:
    while len(stack) > 0 and stack[-1] < v:
        stack.pop()
    answer += len(stack)
    if stack and stack[-1] > v:
        stack.append(v)
    elif not stack:
        stack.append(v)
stack = []
for v in reversed(heights):
    while len(stack) > 0 and stack[-1] < v:
        stack.pop()
    answer += len(stack)
    if stack and stack[-1] > v:
        stack.append(v)
    elif not stack:
        stack.append(v)
print(answer)
