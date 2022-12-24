from collections import deque
def solution(t, p):
    cnt = 0
    cache = deque()
    for i in t:
        cache.append(i)
        if len(cache) == len(p):
            if int(''.join(cache)) <= int(p):
                cnt += 1
            cache.popleft()
    return cnt