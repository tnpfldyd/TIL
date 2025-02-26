import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().rstrip()
    
    if len(command) > 1:
        _, x = map(int, command.split())
        stack.append(x)
    else:
        command = int(command)
        if command == 2:
            print(stack.pop() if stack else -1)
        elif command == 3:
            print(len(stack))
        elif command == 4:
            print(1 if not stack else 0)
        elif command == 5:
            print(stack[-1] if stack else -1)