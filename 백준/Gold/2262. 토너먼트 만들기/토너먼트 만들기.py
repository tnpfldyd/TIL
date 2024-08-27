n = int(input())
players = list(map(int, input().split()))
min_score = 0

max_rank = n
for _ in range(n - 1):
    idx = players.index(max_rank)
    
    if idx == 0:
        min_score += players[idx] - players[idx + 1]
    elif idx == len(players) - 1:
        min_score += players[idx] - players[idx - 1]
    else:
        min_score += min(players[idx] - players[idx - 1], players[idx] - players[idx + 1])
    
    players.pop(idx)
    max_rank -= 1

print(min_score)