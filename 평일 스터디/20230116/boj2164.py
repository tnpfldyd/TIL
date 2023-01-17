from collections import deque

cards = deque([x for x in range(1, int(input()) + 1)])

while cards:
    x = cards.popleft()
    if not cards:
        print(x)
        break
    cards.append(cards.popleft())