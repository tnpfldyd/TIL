import sys
input = sys.stdin.readline
a, b, c = input(), input(), input()
print(int(a) + int(b) - int(c))
print(int(a.strip() + b.strip()) - int(c))