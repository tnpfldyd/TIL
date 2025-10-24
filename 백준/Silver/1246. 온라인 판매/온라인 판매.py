import sys
input = sys.stdin.readline

N, M = map(int, input().split())
prices = [int(input()) for _ in range(M)]

prices.sort()

max_profit = 0
best_price = 0

for price in prices:
    sell_count = 0
    for p in prices:
        if p >= price:
            sell_count += 1
    
    sell_count = min(sell_count, N)
    profit = price * sell_count
    
    if profit > max_profit:
        max_profit = profit
        best_price = price

print(best_price, max_profit)