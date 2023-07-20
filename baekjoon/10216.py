import sys
input = sys.stdin.readline
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    pa, pb = find(a), find(b)
    if pa < pb:
        pa, pb = pb, pa
    parent[pa] = pb

T = int(input())
for _ in range(T):
    v = []
    num = int(input())
    parent = [i for i in range(num)]
    for _ in range(num):
        x, y, r = map(int, input().split())
        v.append((x, y, r))
    
    result = num
    for i in range(num - 1):
        for j in range(i + 1, num):
            fx, fy, fr = v[i]
            sx, sy, sr = v[j]
            d1 = (fr + sr) ** 2
            d2 = (fx - sx) ** 2 + (fy - sy) ** 2
            if d1 >= d2 and find(i) != find(j):
                union(i, j)
                result -= 1
    
    print(result)