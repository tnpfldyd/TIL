import sys
input = sys.stdin.readline

n = int(input())
nums = [input().strip() for _ in range(n)]

length = len(nums[0])

for k in range(1, length + 1):
    s = set()
    for num in nums:
        s.add(num[-k:])
    if len(s) == n:
        print(k)
        break