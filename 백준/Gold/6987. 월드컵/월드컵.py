import sys

input = sys.stdin.readline

games = []
for i in range(5):
    for j in range(i + 1, 6):
        games.append((i, j))

def dfs(idx):
    if idx == 15:
        return True

    a, b = games[idx]

    if result[a][0] > 0 and result[b][2] > 0:
        result[a][0] -= 1
        result[b][2] -= 1
        if dfs(idx + 1):
            return True
        result[a][0] += 1
        result[b][2] += 1

    if result[a][1] > 0 and result[b][1] > 0:
        result[a][1] -= 1
        result[b][1] -= 1
        if dfs(idx + 1):
            return True
        result[a][1] += 1
        result[b][1] += 1

    if result[a][2] > 0 and result[b][0] > 0:
        result[a][2] -= 1
        result[b][0] -= 1
        if dfs(idx + 1):
            return True
        result[a][2] += 1
        result[b][0] += 1

    return False

answers = []

for _ in range(4):
    data = list(map(int, input().split()))
    result = [data[i:i+3] for i in range(0, 18, 3)]

    valid = True
    win = draw = lose = 0

    for w, d, l in result:
        if w + d + l != 5:
            valid = False
        win += w
        draw += d
        lose += l

    if win != lose or draw % 2 != 0:
        valid = False

    if valid and dfs(0):
        answers.append('1')
    else:
        answers.append('0')

print(" ".join(answers))