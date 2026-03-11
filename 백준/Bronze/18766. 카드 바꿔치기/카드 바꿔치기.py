import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    before = input().split()
    after = input().split()

    if Counter(before) == Counter(after):
        print("NOT CHEATER")
    else:
        print("CHEATER")