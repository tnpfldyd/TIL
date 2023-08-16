def comb(layer, l, r):
    if layer == 7:
        return
    m = (l + r) // 2
    games[layer] += 'A' * (m - l) + 'B' * (r - m)
    comb(layer + 1, l, m)
    comb(layer + 1, m, r)

N = int(input())
games = ['' for _ in range(7)]

comb(0, 0, N)
allB = 'B' * N
ans = 'B' * (N - 1) + 'A'
for i in range(7):
    if games[i] == allB:
        print(ans)
    else:
        print(games[i])
