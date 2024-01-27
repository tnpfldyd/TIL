infix = input()
result = ''
stack = []
first = ['*', '/']
second = ['+', '-']
for character in infix:
    if character == '(':
        stack.append(character)
    elif character == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    elif character in first:
        while stack and stack[-1] in first:
            result += stack.pop()
        stack.append(character)
    elif character in second:
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(character)
    else:
        result += character

while stack:
    result += stack.pop()

print(result)