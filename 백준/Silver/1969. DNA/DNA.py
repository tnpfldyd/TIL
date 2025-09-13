import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dnas = [input().strip() for _ in range(n)]

result_dna = ""
total_hd = 0

for i in range(m):
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
    for j in range(n):
        nucleotide = dnas[j][i]
        counts[nucleotide] += 1
    
    max_count = -1
    best_char = ''
    
    for char in ['A', 'C', 'G', 'T']:
        if counts[char] > max_count:
            max_count = counts[char]
            best_char = char
            
    result_dna += best_char
    
    total_hd += (n - max_count)

print(result_dna)
print(total_hd)