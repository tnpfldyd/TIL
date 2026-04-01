import sys
input = sys.stdin.readline

a, o, b = int(input()), input().strip(), int(input())
print(a + b if o == '+' else a * b)