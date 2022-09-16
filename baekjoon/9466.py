import sys
sys.setrecursionlimit(10**9)
def dfs(s):
    global result
    temp.append(s)
    visited[s] = True
    next = per_num[s]
    if visited[next]: 
        if next in temp:
            idx = temp.index(next)
            result += len(temp[idx:])
        return
    else:
        dfs(next)
case = int(input())
for _ in range(case):
    person = int(input())
    per_num = [0] + list(map(int, input().split()))
    result = 0
    visited = [False] * (person + 1)
    for i in range(1, person + 1):
        if not visited[i]:
            temp = []
            dfs(i)
    print(person - result)