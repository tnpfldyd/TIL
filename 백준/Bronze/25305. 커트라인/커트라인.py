N, k = map(int, input().split())
numbers = sorted(list(map(int, input().split())), reverse=True)
print(numbers[k - 1])