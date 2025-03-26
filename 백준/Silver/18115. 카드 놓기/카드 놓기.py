import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

cards = deque()

for i in range(N - 1, -1, -1):
    if A[i] == 1:
        cards.appendleft(abs(i - N))
    elif A[i] == 2:
        cards.insert(1, abs(i - N))
    elif A[i] == 3:
        cards.append(abs(i - N))

print(*cards)