import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(int, input().split()))

l = 0
odd = 0
answer = 0

for r in range(N):
    if S[r] % 2 == 1:
        odd += 1

    while odd > K:
        if S[l] % 2 == 1:
            odd -= 1
        l += 1

    answer = max(answer, (r - l + 1) - odd)

print(answer)