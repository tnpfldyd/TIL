ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
stack = []
result = 0
for i in ingredient:
    stack.append(i)
    if len(stack) > 3 and i == 1:
        if stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
            result += 1
            for j in range(4):
                stack.pop()
print(result)