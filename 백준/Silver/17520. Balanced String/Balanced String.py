mod = 16769023

n = int(input())
result = 2

for i in range(2, n + 1):
    if i % 2:
        result = (result * 2) % mod

print(result)