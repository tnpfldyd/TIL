import sys
input = sys.stdin.readline

N, R = map(int, input().split())
cities = {name: i for i, name in enumerate(input().split())}
M = int(input())
tourist_cities = input().split()

K = int(input())
usual = [[float('inf')] * N for _ in range(N)]
railro = [[float('inf')] * N for _ in range(N)]

for _ in range(K):
    t, s, e, c = input().split()
    start, end = cities[s], cities[e]
    c = float(c)

    usual[start][end] = min(usual[start][end], c)
    usual[end][start] = min(usual[end][start], c)

    if t in {"Mugunghwa", "ITX-Saemaeul", "ITX-Cheongchun"}:
        railro[start][end] = min(railro[start][end], 0)
        railro[end][start] = min(railro[end][start], 0)
    elif t in {"S-Train", "V-Train"}:
        railro[start][end] = min(railro[start][end], c * 0.5)
        railro[end][start] = min(railro[end][start], c * 0.5)
    else:
        railro[start][end] = min(railro[start][end], c)
        railro[end][start] = min(railro[end][start], c)

for k in range(N):
    for i in range(N):
        for j in range(N):
            usual[i][j] = min(usual[i][j], usual[i][k] + usual[k][j])
            railro[i][j] = min(railro[i][j], railro[i][k] + railro[k][j])

usual_cost, railro_cost = 0, R
for i in range(M - 1):
    s, e = cities[tourist_cities[i]], cities[tourist_cities[i + 1]]
    usual_cost += usual[s][e]
    railro_cost += railro[s][e]
print("Yes" if usual_cost > railro_cost else "No")