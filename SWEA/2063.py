import sys

sys.stdin = open("2063input.txt", "r")

T = int(input())

c = list(map(int, input().split()))
c.sort()
print((c[T//2]))