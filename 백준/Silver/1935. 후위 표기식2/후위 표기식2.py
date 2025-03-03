import sys

input = sys.stdin.readline

N = int(input())
expression = input().strip()
values = [int(input()) for _ in range(N)]

stack = []

for char in expression:
    if char.isalpha():
        idx = ord(char) - ord('A')
        stack.append(values[idx])
    else:
        b = stack.pop()
        a = stack.pop()
        if char == '+':
            stack.append(a + b)
        elif char == '-':
            stack.append(a - b)
        elif char == '*':
            stack.append(a * b)
        elif char == '/':
            stack.append(a / b)

print(f"{stack[0]:.2f}")