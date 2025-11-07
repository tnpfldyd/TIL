import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())

broken = [False] * (N + 1)
for _ in range(B):
    num = int(input())
    broken[num] = True

count = 0
for i in range(1, K + 1):
    if broken[i]:
        count += 1

min_repair = count

for i in range(2, N - K + 2):
    if broken[i - 1]:
        count -= 1
    if broken[i + K - 1]:
        count += 1
    min_repair = min(min_repair, count)

print(min_repair)