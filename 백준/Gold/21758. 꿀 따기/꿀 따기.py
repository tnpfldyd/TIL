
N = int(input())
hunny = [0] + list(map(int, input().split()))
sums = [0] * (N + 1)

for i in range(N + 1):
    sums[i] = hunny[i] + sums[i - 1]

answer = 0
for i in range(2, N):
    answer = max(
        answer,
        sums[N] - hunny[1] - hunny[i] + sums[N] - sums[i],
        sums[N] - hunny[N] - hunny[i] + sums[i - 1],
        sums[i] - hunny[1] + sums[N] - sums[i - 1] - hunny[N]
    )
print(answer)