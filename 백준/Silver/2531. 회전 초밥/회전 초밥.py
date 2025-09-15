import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))

max_types = 0
count = [0] * (d + 1)
unique_count = 0

for i in range(k):
    if count[sushi[i]] == 0:
        unique_count += 1
    count[sushi[i]] += 1

current_types = unique_count
if count[c] == 0:
    current_types += 1
max_types = current_types

for i in range(N):
    remove_idx = i
    add_idx = (i + k) % N
    
    count[sushi[remove_idx]] -= 1
    if count[sushi[remove_idx]] == 0:
        unique_count -= 1
    
    if count[sushi[add_idx]] == 0:
        unique_count += 1
    count[sushi[add_idx]] += 1
    
    current_types = unique_count
    if count[c] == 0:
        current_types += 1
    
    max_types = max(max_types, current_types)

print(max_types)