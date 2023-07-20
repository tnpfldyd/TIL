N, M = map(int, input().split())
sums = 0
cnt = [0] * M
numbers = list(map(int, input().split()))

for number in numbers:
    sums += number
    cnt[sums % M] += 1

result = cnt[0]
for i in range(M):
    result += cnt[i] * (cnt[i] - 1) // 2
print(result)