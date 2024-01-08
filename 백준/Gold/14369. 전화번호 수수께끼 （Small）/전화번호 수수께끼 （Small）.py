from collections import defaultdict
import sys
input = sys.stdin.readline

alphabet = [('Z', 'ZERO', 0), ('X', 'SIX', 6), ('G', 'EIGHT', 8),
     ('S', 'SEVEN', 7), ('V', 'FIVE', 5), ('F', 'FOUR', 4),
     ('I', 'NINE', 9), ('W', 'TWO', 2), ('R', 'THREE', 3),
     ('O', 'ONE', 1)]

def process_case(case_num, input_str):
    count_dict = defaultdict(int)
    result = [0] * 10
    for char in input_str:
        count_dict[char] += 1
    for key, word, index in alphabet:
        if count_dict[key]:
            result[index] = count_dict[key]
            for char in word:
                count_dict[char] -= result[index]
        result[index] *= str(index)
    print(f"Case #{case_num}: {''.join(result)}")

for t in range(int(input())):
    process_case(t + 1, input().strip())