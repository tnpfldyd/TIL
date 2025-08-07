N = int(input())
numbers = list(map(int, input().split()))

unique_sorted = sorted(set(numbers))
print(*unique_sorted)