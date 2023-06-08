s = input()
stack = []
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    elif s[i] == ')':
        cnt = 0
        while True:
            x = stack.pop()
            if x == '(':
                break
            cnt += x
        stack.append(int(stack.pop()) * cnt)
    elif i < len(s) - 1 and s[i + 1] == '(':
        stack.append(int(s[i]))
    else:
        stack.append(1)

print(sum(stack))