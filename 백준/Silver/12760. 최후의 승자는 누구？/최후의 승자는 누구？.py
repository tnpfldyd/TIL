import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cards = []
for _ in range(N):
    arr = list(map(int, input().split()))
    arr.sort()
    cards.append(arr)

scores = [0] * N
idx = [M - 1] * N

for _ in range(M):
    played = []
    turn_max = -1

    for i in range(N):
        value = cards[i][idx[i]]
        idx[i] -= 1
        played.append(value)
        turn_max = max(turn_max, value)

    for i in range(N):
        if played[i] == turn_max:
            scores[i] += 1

best = max(scores)

winners = [str(i + 1) for i in range(N) if scores[i] == best]
print(" ".join(winners))