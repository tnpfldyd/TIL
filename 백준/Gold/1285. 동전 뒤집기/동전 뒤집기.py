import sys
input = sys.stdin.readline

def flip_rows(row_mask):
    for i in range(N):
        if row_mask & (1 << i):
            rows[i] = ((1 << N) - 1) ^ rows[i]

def calculate_minimum_flips(row_mask):
    value = 0
    flip_rows(row_mask)
    
    for i in range(N):
        heads_count = 0
        for j in range(N):
            if rows[j] & (1 << i):
                heads_count += 1
        value += min(heads_count, N - heads_count)
    
    flip_rows(row_mask)
    return value

N = int(input())
rows = [0] * N
for i in range(N):
    coins = input().strip()
    for j in range(N):
        if coins[j] == 'T':
            rows[i] += (1 << j)

min_flips = N ** 2
for i in range(1 << N):
    min_flips = min(min_flips, calculate_minimum_flips(i))

print(min_flips)