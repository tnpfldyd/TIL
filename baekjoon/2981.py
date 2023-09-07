import sys, math
input = sys.stdin.readline
N = int(input())
numbers = sorted((int(input())) for _ in range(N))
diffs = [numbers[i] - numbers[i - 1] for i in range(1, N)]
prev = diffs[0]

for i in range(1, N - 1):
    prev = math.gcd(prev, diffs[i])

answer = set()
for i in range(2, int(prev ** 0.5) + 1):
    if not prev % i:
        answer.add(i)
        answer.add(prev // i)
answer.add(prev)
answer = sorted(list(answer))
print(*answer)
