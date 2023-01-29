string = input()
stack = []
answer, cnt = 0, 1
left, right = {'(' : 2, '[' : 3}, {')' : 2, ']' : 3}
for i in range(len(string)):
    if string[i] in left:
        stack.append(string[i])
        cnt *= left[string[i]]
    else:
        if not stack or left[stack[-1]] != right[string[i]]:
            answer = 0
            break
        if left.get(string[i-1]) == right.get(string[i]):
            answer += cnt
        stack.pop()
        cnt //= right[string[i]]
print(0 if stack else answer)