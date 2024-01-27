import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print('1 0' if int(input()) <= 1 else '0 1')