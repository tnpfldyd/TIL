s, p = map(int, input().split())
dna = input()
min_count = list(map(int, input().split()))

current_count = [0] * 4
dna_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

for i in range(p):
    current_count[dna_map[dna[i]]] += 1

valid = 0
for i in range(4):
    if current_count[i] >= min_count[i]:
        valid += 1

result = 1 if valid == 4 else 0

for i in range(p, s):
    current_count[dna_map[dna[i]]] += 1
    if current_count[dna_map[dna[i]]] == min_count[dna_map[dna[i]]]:
        valid += 1
    
    left_char = dna[i - p]
    current_count[dna_map[left_char]] -= 1
    if current_count[dna_map[left_char]] == min_count[dna_map[left_char]] - 1:
        valid -= 1
    
    if valid == 4:
        result += 1

print(result)