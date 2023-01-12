def solution(d, budget):
    cnt = 0
    d.sort(reverse=True)
    while budget > 0 and d:
        x = d.pop()
        budget -= x
        cnt += 1
    if budget < 0:
        cnt -= 1
    return cnt