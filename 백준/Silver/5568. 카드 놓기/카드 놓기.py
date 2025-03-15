import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]
perms = permutations(cards, k)
unique_numbers = set()

for perm in perms:
    unique_numbers.add(''.join(perm))

print(len(unique_numbers))