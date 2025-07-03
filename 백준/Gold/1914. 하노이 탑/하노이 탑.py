import sys
sys.setrecursionlimit(10**6)

n = int(input())

moves = []

def hanoi(n, start, end, via):
    if n == 1:
        moves.append((start, end))
        return
    hanoi(n - 1, start, via, end)
    moves.append((start, end))
    hanoi(n - 1, via, end, start)

print(2 ** n - 1)

if n <= 20:
    hanoi(n, 1, 3, 2)
    for a, b in moves:
        print(a, b)