import sys
input = sys.stdin.readline

N = int(input())
prices = []
for _ in range(N):
    prices.append(int(input()))

prices.sort(reverse=True)

total = 0
i = 0
while i < N:
    if i + 2 < N:
        total += prices[i] + prices[i + 1]
        i += 3
    else:
        while i < N:
            total += prices[i]
            i += 1

print(total)