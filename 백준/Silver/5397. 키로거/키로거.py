import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().strip()
    left = []
    right = []
    for char in s:
        if char == '-' and left:
            left.pop()
        elif char == '<' and left:
            right.append(left.pop())
        elif char == '>' and right:
            left.append(right.pop())
        elif char not in '-<>':
            left.append(char)
    print(''.join(left + right[::-1]))