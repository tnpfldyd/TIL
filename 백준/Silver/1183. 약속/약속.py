import sys
input = sys.stdin.readline

N = int(input())
C = []
for _ in range(N):
    A, B = map(int, input().split())
    C.append(B - A)

C.sort()

if N % 2 == 1:
    print(1)
else:
    L = C[N // 2 - 1]
    R = C[N // 2]
    print(R - L + 1)