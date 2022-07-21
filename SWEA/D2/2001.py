import sys

sys.stdin = open("2001input.txt", "r")

T = int(input())
for i in range(1, T+1):
    a, b = map(int, input().split())
    c = [list(map(int, input().split())) for _ in range(a)]
    print(c)