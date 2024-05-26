from collections import defaultdict, deque
import sys
input = sys.stdin.readline

Q = int(input())

dic = defaultdict(deque)
result = 0
for _ in range(Q):
    q, name, c, *nums = input().split()
    q, c, nums = int(q), int(c), list(map(int, nums))
    if q == 1:
        for num in nums:
            dic[name].append(num)
    else:
        if name not in dic:
            continue
        dic[name] = deque(sorted(dic[name], reverse=True))
        for _ in range(min(c, len(dic[name]))):
            result += dic[name].popleft()

print(result)