import sys
input = sys.stdin.readline

N, K = map(int, input().split())
need = []

for _ in range(N):
    A, B = map(int, input().split())
    need.append(max(0, B - A))

need.sort()
print(need[K - 1])