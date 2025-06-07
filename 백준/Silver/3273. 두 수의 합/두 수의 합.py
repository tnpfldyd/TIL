n = int(input())
nums = list(map(int, input().split()))
x = int(input())

visited = set()
count = 0

for num in nums:
    if x - num in visited:
        count += 1
    visited.add(num)

print(count)