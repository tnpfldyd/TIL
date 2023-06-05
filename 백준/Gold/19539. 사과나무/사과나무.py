N = int(input())

numbers = list(map(int, input().split()))

total = sum(numbers)
cnt = sum(map(lambda x : x // 2, numbers))
print("NO" if total % 3 else "YES" if cnt >= total / 3 else "NO")