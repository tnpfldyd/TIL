moves = []

def hanoi(n, start, end, aux):
    if n == 1:
        moves.append((start, end))
    else:
        hanoi(n - 1, start, aux, end)
        moves.append((start, end))
        hanoi(n - 1, aux, end, start)

N = int(input())
hanoi(N, 1, 3, 2)
print(len(moves))
for move in moves:
    print(*move)