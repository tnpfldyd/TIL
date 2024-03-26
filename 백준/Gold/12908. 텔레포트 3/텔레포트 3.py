xs, ys = map(int, input().split())
xe, ye = map(int, input().split())
coordinates = [(xs, ys), (xe, ye)]
dist = [[float('inf')] * 8 for _ in range(8)]

for i in (2, 4, 6):
    x1, y1, x2, y2 = map(int, input().split())
    dist[i][i + 1] = 10
    dist[i + 1][i] = 10
    coordinates.extend([(x1, y1), (x2, y2)])

for i in range(8):
    for j in range(8):
        if i == j:
            dist[i][j] = 0
            continue
        len_ = abs(coordinates[i][0] - coordinates[j][0]) + abs(coordinates[i][1] - coordinates[j][1])
        dist[i][j] = min(dist[i][j], len_)
        dist[j][i] = min(dist[j][i], len_)

for k in range(8):
    for i in range(8):
        for j in range(8):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

print(dist[0][1])