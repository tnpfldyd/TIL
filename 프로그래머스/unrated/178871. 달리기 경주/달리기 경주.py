def solution(players, callings):
    players_dic = {name : idx for idx, name in enumerate(players)}
    for call in callings:
        x, y = players_dic[call], players_dic[call] - 1
        players[x], players[y] = players[y], players[x]
        players_dic[players[x]] += 1; players_dic[players[y]] -= 1
        
    return players