s = input()
cards = set()
counts = {'P': 0, 'K': 0, 'H': 0, 'T': 0}

for i in range(0, len(s), 3):
    card = s[i:i+3]
    if card in cards:
        print("GRESKA")
        exit()
    cards.add(card)
    counts[card[0]] += 1

print(13 - counts['P'], 13 - counts['K'], 13 - counts['H'], 13 - counts['T'])