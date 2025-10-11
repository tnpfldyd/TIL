n = int(input())
a = list(map(int, input().split()))

even_idx = [i for i, x in enumerate(a) if x % 2 == 0]
odd_idx = [i for i, x in enumerate(a) if x % 2 == 1]

cost_even_left = sum(abs(even_idx[i] - i) for i in range(len(even_idx)))
cost_odd_left = sum(abs(odd_idx[i] - i) for i in range(len(odd_idx)))

print(min(cost_even_left, cost_odd_left))