import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    
    max_profit = 0
    max_price = 0
    
    for i in range(N - 1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            max_profit += max_price - prices[i]
    
    print(max_profit)