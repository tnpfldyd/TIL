import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
print(A[K - 1])