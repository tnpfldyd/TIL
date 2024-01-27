N = int(input())
numbers = list(map(int, input().split()))

stacks = [[0] for _ in range(4)]
flag = False
for number in numbers:
    flag = False
    for i in range(4):
        stack = stacks[i]
        if stack[-1] < number:
            stack.append(number)
            flag = True
            break

print('YES' if flag else 'NO')