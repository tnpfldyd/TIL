import sys
import math
input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

distances = []
for i in range(N):
    distances.append(abs(A[i] - S))

result = distances[0]
for i in range(1, N):
    result = math.gcd(result, distances[i])

print(result)