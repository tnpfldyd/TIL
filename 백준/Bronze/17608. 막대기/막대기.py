import sys
input = sys.stdin.readline

N = int(input())
heights = [int(input()) for _ in range(N)]

count = 0
max_height = 0

for h in reversed(heights):
    if h > max_height:
        count += 1
        max_height = h

print(count)