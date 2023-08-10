from collections import defaultdict
N, K = map(int, input().split())
numbers = map(int, input().split())
sums = defaultdict(int)
sums[0] = 1
answer = pre = 0

for number in numbers:
    pre += number
    if pre - K in sums:
        answer += sums[pre - K]
    sums[pre] += 1

print(answer)