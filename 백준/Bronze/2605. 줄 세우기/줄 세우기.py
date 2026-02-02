n = int(input())
nums = list(map(int, input().split()))

line = []

for i in range(n):
    k = nums[i]
    pos = len(line) - k
    line.insert(pos, i + 1)

print(*line)