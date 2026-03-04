import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(1, N + 1):
    w, h = map(int, input().split())
    s = w*w + h*h
    arr.append((-s, i))

arr.sort()

for _, idx in arr:
    print(idx)