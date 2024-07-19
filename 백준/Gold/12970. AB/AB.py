import sys
input = sys.stdin.readline

n, target_pairs = map(int, input().split())
sequence = ['B'] * n
current_pairs = 0
max_possible_pairs = 0

for i in range(n // 2 + 1):
    max_possible_pairs = max(max_possible_pairs, i * (n - i))

if max_possible_pairs < target_pairs:
    print(-1)
    exit()

while current_pairs != target_pairs:
    index = n - 1
    current_pairs -= sequence.count('A')
    sequence[index] = 'A'
    
    while index > 0 and sequence[index - 1] == 'B' and current_pairs != target_pairs:
        sequence[index] = 'B'
        index -= 1
        sequence[index] = 'A'
        current_pairs += 1

print(''.join(sequence))
