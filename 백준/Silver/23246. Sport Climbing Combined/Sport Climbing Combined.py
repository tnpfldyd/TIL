import sys
input = sys.stdin.readline
n = int(input())
players = []

for _ in range(n):
    b, p, q, r = map(int, input().split())
    product = p * q * r
    total = p + q + r
    players.append((product, total, b))

players.sort()

print(players[0][2], players[1][2], players[2][2])