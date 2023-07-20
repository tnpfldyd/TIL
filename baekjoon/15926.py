
N = int(input())
check = input()
stack = [-1]
answer = 0

for i in range(N):
    if check[i] == '(':
        stack.append(i)
    else:
        if stack:
            stack.pop()
        if stack:
            answer = max(answer, i - stack[-1])
        else:
            stack.append(i)
print(answer)