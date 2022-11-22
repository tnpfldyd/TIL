from heapq import heappop, heappush
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    last_case = int(input())
    last_list = list(map(int, input().strip().split()))
    matrix = [[] for _ in range(last_case)]
    visited = [0] * last_case
    for i in range(last_case):
        for j in range(i+1, last_case):
            matrix[last_list[i]-1].append(last_list[j]-1)
            visited[last_list[j]-1] += 1
    change_case = int(input())
    for i in range(change_case):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        if a in matrix[b]:
            matrix[b].remove(a)
            matrix[a].append(b)
            visited[b] += 1
            visited[a] -= 1
        else:
            matrix[a].remove(b)
            matrix[b].append(a)
            visited[a] += 1
            visited[b] -= 1
    start = []
    for i in range(last_case):
        if not visited[i]:
            heappush(start, i)
    result = []
    while start:
        x = heappop(start)
        result.append(x+1)
        for i in matrix[x]:
            visited[i] -= 1
            if not visited[i]:
                heappush(start, i)
    if len(result) == last_case:
        print(*result)
    else:
        print('IMPOSSIBLE')