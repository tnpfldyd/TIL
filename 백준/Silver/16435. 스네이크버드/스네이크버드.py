import sys
input = sys.stdin.readline

N, L = map(int, input().split())
heights = list(map(int, input().split()))

heights.sort()

length = L
for height in heights:
    if length >= height:
        length += 1

print(length)