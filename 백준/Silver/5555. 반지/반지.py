import sys
input = sys.stdin.readline

target = input().strip()
N = int(input())

count = 0
for _ in range(N):
    ring = input().strip()
    extended_ring = ring + ring
    if target in extended_ring:
        count += 1

print(count)