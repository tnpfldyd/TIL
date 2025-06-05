import sys
input = sys.stdin.readline

N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]
total_cost = 0

for i in range(N - 1):
    if prices[i] < min_price:
        min_price = prices[i]
    total_cost += min_price * distances[i]

print(total_cost)