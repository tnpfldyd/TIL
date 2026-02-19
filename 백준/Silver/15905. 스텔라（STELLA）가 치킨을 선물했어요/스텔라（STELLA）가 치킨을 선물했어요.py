import sys
input = sys.stdin.readline
n = int(input())
players = []
for _ in range(n):
    solved, penalty = map(int, input().split())
    players.append((-solved, penalty))

players.sort()
fifth_solved = players[4][0]

print(sum(1 for s, p in players[5:] if s == fifth_solved))