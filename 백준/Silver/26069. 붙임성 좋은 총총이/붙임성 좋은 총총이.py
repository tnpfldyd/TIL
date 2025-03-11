import sys
input = sys.stdin.readline

N = int(input())
dancing = {"ChongChong"}

for _ in range(N):
    A, B = input().split()
    if A in dancing or B in dancing:
        dancing.add(A)
        dancing.add(B)

print(len(dancing))