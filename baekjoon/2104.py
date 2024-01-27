N = int(input())
numbers = list(map(int, input().split())) + [0]

cumulativeSum = [0]
for i in range(N):
  cumulativeSum.append(cumulativeSum[-1] + numbers[i])

stack = []
result = 0

for i in range(N + 1):
  curHeight = numbers[i]
  cur = i
  while stack and stack[-1][0] >= curHeight:
    height, cur = stack.pop()
    result = max(result, (cumulativeSum[i] - cumulativeSum[cur]) * height)
  stack.append((curHeight, cur))
print(result)