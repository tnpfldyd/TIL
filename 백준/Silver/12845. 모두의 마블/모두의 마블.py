n = int(input())
cards = list(map(int, input().split()))

total_gold = 0

while len(cards) > 1:
    max_idx = max(range(len(cards)), key=lambda i: cards[i])
    max_card = cards[max_idx]

    if max_idx == 0:
        merge_idx = 1
    elif max_idx == len(cards) - 1:
        merge_idx = max_idx - 1
    else:
        left_card = cards[max_idx - 1]
        right_card = cards[max_idx + 1]
        merge_idx = max_idx - 1 if left_card < right_card else max_idx + 1

    merge_card = cards[merge_idx]
    total_gold += max_card + merge_card

    cards.pop(merge_idx)

print(total_gold)