import sys
input = sys.stdin.readline

N = int(input())
prices = list(map(int, input().split()))
max_price, max_profit = 0, 0

for i in range(N-1, -1, -1):
    max_price = max(max_price, prices[i])
    max_profit = max(max_profit, max_price - prices[i])

print(max_profit)