from collections import deque
t = "500220839878"
p = "7"
cnt = 0
cache = deque()
for i in t:
    cache.append(i)
    if len(cache) == len(p):
        if int(''.join(cache)) <= int(p):
            cnt += 1
        cache.popleft()
print(cnt)