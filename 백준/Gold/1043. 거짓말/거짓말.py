import sys
input = sys.stdin.readline

N, M = map(int, input().split())
v = [[] for _ in range(M)]
know = list(map(int, input().split()))[1:]
parent = [i for i in range(N + 1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    parent[x] = y
for i in range(M):
    p, *nums = map(int, input().split())
    for j in range(p - 1):
        union(nums[j], nums[j + 1])
    v[i] = nums

cnt = 0

for nums in v:
    flag = False
    for num in nums:
        if flag:
            break
        for t in know:
            if find(num) == find(t):
                flag = True
                break
    if flag:
        cnt += 1
print(M - cnt)