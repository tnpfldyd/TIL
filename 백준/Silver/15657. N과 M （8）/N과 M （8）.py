from itertools import combinations_with_replacement

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

for combo in combinations_with_replacement(numbers, m):
    print(' '.join(map(str, combo)))