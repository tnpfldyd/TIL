import sys
input = sys.stdin.readline

N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]
max_profit, best_price = 0, 0
checked_prices = set()
for price, _ in people:
    if price in checked_prices:
        continue
    checked_prices.add(price)
    profit = 0
    for p, m in people:
        if p >= price and price > m:
            profit += price - m
    if profit > max_profit:
        max_profit = profit
        best_price = price
    elif profit == max_profit and profit != 0:
        best_price = min(best_price, price)

print(best_price if max_profit > 0 else 0)