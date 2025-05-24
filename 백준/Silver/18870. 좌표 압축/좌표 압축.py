import sys

input = sys.stdin.readline

n = int(input())
coords = list(map(int, input().split()))
sorted_unique = sorted(set(coords))
compressed = {x: i for i, x in enumerate(sorted_unique)}
print(' '.join(str(compressed[x]) for x in coords))