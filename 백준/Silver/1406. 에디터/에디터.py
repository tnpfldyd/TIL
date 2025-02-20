import sys
input = sys.stdin.readline

initial_string = input().strip()

M = int(input().strip())

left_stack = list(initial_string)
right_stack = []

for _ in range(M):
    command = input().strip()
    if command == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command == 'B':
        if left_stack:
            left_stack.pop()
    elif command[0] == 'P':
        char = command[2]
        left_stack.append(char)

print(''.join(left_stack + right_stack[::-1]))