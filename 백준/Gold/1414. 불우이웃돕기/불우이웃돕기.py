import sys
input = sys.stdin.readline

def find(parents, a):
    if parents[a] == a:
        return a
    parents[a] = find(parents, parents[a])
    return parents[a]

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

def solution():
    n = int(input())
    total = 0
    parents = [i for i in range(n+1)]
    edges = []
    
    for i in range(1, n+1):
        line = input().strip()
        for j in range(1, n+1):
            c = line[j-1]
            if c.islower():
                cost = ord(c) - ord('a') + 1
                edges.append((cost, i, j))
                total += cost
            elif c.isupper():
                cost = ord(c) - ord('A') + 27
                edges.append((cost, i, j))
                total += cost
    
    edges.sort()
    
    for edge in edges:
        cost, node1, node2 = edge
        if find(parents, node1) != find(parents, node2):
            union(parents, node1, node2)
            total -= cost
    
    p = find(parents, 1)
    for i in range(2, n+1):
        if find(parents, i) != p:
            print(-1)
            return
    
    print(total)

solution()