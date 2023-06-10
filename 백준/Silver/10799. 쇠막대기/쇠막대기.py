bracket = input()

result = 0
stack = []

for i in range(len(bracket)):
    if bracket[i] == '(':
        stack.append(1)
    else:
        stack.pop()
        if bracket[i - 1] == '(':
            result += len(stack)
        else:
            result += 1

print(result)