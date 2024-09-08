import sys
import math

input = sys.stdin.readline
n = int(input())

expiration_days = list(map(int, input().split()))
usage_days = list(map(int, input().split()))

coupons = []
for exp, use in zip(expiration_days, usage_days):
    coupons.append([exp, use])

coupons = sorted(coupons, key=lambda x: (x[1], x[0]))

current_expiration = coupons[0][0]
current_usage_day = coupons[0][1]
extension_count = 0

for i in range(n):
    if current_usage_day > coupons[i][0]:
        extensions_needed = math.ceil((current_usage_day - coupons[i][0]) / 30)
        extension_count += extensions_needed
        coupons[i][0] += extensions_needed * 30
    
    current_expiration = max(current_expiration, coupons[i][0])

    if i + 1 < n and coupons[i][1] != coupons[i + 1][1]:
        current_usage_day = max(current_expiration, coupons[i + 1][1])

print(extension_count)