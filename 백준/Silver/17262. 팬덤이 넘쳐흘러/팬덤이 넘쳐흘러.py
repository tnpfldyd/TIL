import sys
input = sys.stdin.readline

N = int(input())

max_s = 0
min_e = 10**9

for _ in range(N):
    s, e = map(int, input().split())
    max_s = max(max_s, s)
    min_e = min(min_e, e)

print(max(0, max_s - min_e))