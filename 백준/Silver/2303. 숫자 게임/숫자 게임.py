import sys
input = sys.stdin.readline

N = int(input())

max_digit = -1
winner = 0

for person in range(1, N + 1):
    cards = list(map(int, input().split()))
    
    person_max = 0
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                digit = (cards[i] + cards[j] + cards[k]) % 10
                person_max = max(person_max, digit)
    
    if person_max >= max_digit:
        max_digit = person_max
        winner = person

print(winner)