import sys
input = sys.stdin.readline

N = int(input())
a = []

for i in range(1, N + 1):
    T, S = map(int, input().split())
    a.append((T / S, i))

a.sort()

for _, idx in a:
    print(idx, end=" ")