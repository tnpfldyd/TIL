n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B_sorted = sorted(B, reverse=True)

S = sum(a * b for a, b in zip(A, B_sorted))
print(S)