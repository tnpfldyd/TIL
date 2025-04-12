weight = {'H': 1, 'C': 12, 'O': 16}
stack = []
formula = input().strip()

for ch in formula:
    if ch in weight:
        stack.append(weight[ch])
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        temp = 0
        while stack and stack[-1] != '(':
            temp += stack.pop()
        stack.pop()
        stack.append(temp)
    elif ch.isdigit():
        num = int(ch)
        temp = stack.pop()
        stack.append(temp * num)

print(sum(stack))