import sys
input = sys.stdin.readline

n = int(input())
players = []
for _ in range(n):
    name, score = input().split()
    players.append((-int(score), name))

players.sort()
print(players[0][1])