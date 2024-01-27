import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
visited = [0] * 1000001
result = [0] * 1000001
for card in cards:
    visited[card] = 1

for card in cards:
    for j in range(card * 2, 1000001, card):
        if visited[j] == 1:
            result[card] += 1
            result[j] -= 1

for card in cards:
    print(result[card], end=" ")