import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
cnt = Counter(nums)

answer = -1
for t in range(N + 1):
    if cnt[t] == t:
        answer = t

print(answer)