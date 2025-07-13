N, M = map(int, input().split())

min_package_price = float('inf')
min_single_price = float('inf')

for _ in range(M):
    package_price, single_price = map(int, input().split())
    min_package_price = min(min_package_price, package_price)
    min_single_price = min(min_single_price, single_price)

packages_needed = (N + 5) // 6
cost_packages_only = packages_needed * min_package_price

cost_singles_only = N * min_single_price

min_cost_combination = float('inf')

for packages in range(packages_needed + 1):
    strings_from_packages = packages * 6
    remaining_strings = max(0, N - strings_from_packages)
    
    cost = packages * min_package_price + remaining_strings * min_single_price
    min_cost_combination = min(min_cost_combination, cost)

result = min(cost_packages_only, cost_singles_only, min_cost_combination)

print(result)