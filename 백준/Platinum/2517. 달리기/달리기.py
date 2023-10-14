import sys
input = sys.stdin.readline

def update(id, value):
    while id <= N:
        tree[id] += value
        id += id & -id

def query(id):
    ret = 0
    while id:
        ret += tree[id]
        id -= id & -id
    return ret

N = int(input())
players = [(int(input()), i) for i in range(1, N + 1)]
players.sort(reverse=True)
answer = [0] * (N + 1)
tree = [0] * (N + 1)

for i in range(N):
    curId = players[i][1]
    update(curId, 1)
    answer[curId] = query(curId)

for i in range(1, N + 1):
    print(answer[i])