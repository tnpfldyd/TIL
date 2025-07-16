from itertools import permutations

def calculate_sum(arr):
    total = 0
    for i in range(len(arr) - 1):
        total += abs(arr[i] - arr[i + 1])
    return total

n = int(input())
arr = list(map(int, input().split()))

max_sum = 0

for perm in permutations(arr):
    current_sum = calculate_sum(perm)
    max_sum = max(max_sum, current_sum)

print(max_sum)