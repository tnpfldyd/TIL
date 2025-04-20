import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
parrots = [deque(input().split()) for _ in range(N)]
L = input().split()

for word in L:
    for parrot in parrots:
        if parrot and parrot[0] == word:
            parrot.popleft()
            break
    else:
        print("Impossible")
        exit()

if all(not p for p in parrots):
    print("Possible")
else:
    print("Impossible")