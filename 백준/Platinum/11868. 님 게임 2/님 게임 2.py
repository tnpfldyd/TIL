import sys
input = sys.stdin.readline
N = int(input())
t = 0
numbers = tuple(map(int, input().split()))
for number in numbers:
    t ^= number
print('koosaga' if t else 'cubelover')