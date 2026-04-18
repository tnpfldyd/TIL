import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        print(a + b, a * b)