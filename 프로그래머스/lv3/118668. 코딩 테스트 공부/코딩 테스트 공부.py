from heapq import heappop, heappush

def solution(alp, cop, problems):
    max_alp, max_cop = sorted(problems)[-1][0], sorted(problems, key= lambda x : x[1])[-1][1]
    edges = set()
    problems.append((0, 0, 1, 0, 1)); problems.append((0, 0, 0, 1, 1))
    for a, c, pa, pc, cost in problems:
        if not pa and not pc:
            continue
        edges.add((a, c, pa, pc, cost))
    start = []
    heappush(start, (0, alp, cop))
    visited = set()
    while start:
        cost, x, y = heappop(start)
        x, y = min(x, max_alp), min(y, max_cop)
        if x >= max_alp and y >= max_cop:
            return cost
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for a, c, pa, pc, nc in problems:
            if x >= a and y >= c:
                if (x + pa, y + pc) not in visited:
                    heappush(start, (cost + nc, x + pa, y + pc))