import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    print(max((input().split() for _ in range(N)), key=lambda x: int(x[1]))[0])