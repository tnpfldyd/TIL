import sys
input = sys.stdin.readline

A, B = map(int, input().split())

nums = []

def dfs(x):
    if x > B:
        return
    if x != 0:
        nums.append(x)
    dfs(x * 10 + 4)
    dfs(x * 10 + 7)

dfs(0)
nums.sort(reverse=True)

cnt = 0
for v in nums:
    if v < A:
        break
    cnt += 1

print(cnt)