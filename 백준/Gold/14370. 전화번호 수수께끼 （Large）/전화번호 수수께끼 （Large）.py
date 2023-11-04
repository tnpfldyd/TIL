from collections import defaultdict
import sys
input = sys.stdin.readline

NUMBERS = [('Z', 'ZERO', 0), ('X', 'SIX', 6), ('G', 'EIGHT', 8),
           ('S', 'SEVEN', 7), ('V', 'FIVE', 5), ('F', 'FOUR', 4),
           ('I', 'NINE', 9), ('W', 'TWO', 2), ('R', 'THREE', 3),
           ('O', 'ONE', 1)]

for t in range(int(input())):
    char_count = defaultdict(int)
    result = []

    for char in input().strip():
        char_count[char] += 1

    for key_char, number_str, number in NUMBERS:
        while char_count[key_char] > 0:
            result.append(str(number))
            for char in number_str:
                char_count[char] -= 1

    result.sort()
    print(f"Case #{t+1}: {''.join(result)}")