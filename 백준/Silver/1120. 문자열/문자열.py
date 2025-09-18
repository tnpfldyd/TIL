import sys
input = sys.stdin.readline

A, B = input().split()

min_diff = float('inf')

for start in range(len(B) - len(A) + 1):
    diff = 0
    for i in range(len(A)):
        if A[i] != B[start + i]:
            diff += 1
    min_diff = min(min_diff, diff)

print(min_diff)