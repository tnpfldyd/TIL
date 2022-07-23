import sys

sys.stdin = open("2001input.txt", "r")

T = int(input())
result = 0
for i in range(1, T+1):
    a, b = map(int, input().split())
    for j in range(a):
        c = list(map(int, input().split()))
        