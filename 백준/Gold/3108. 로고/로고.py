import sys
input = sys.stdin.readline

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def meet(a: Rectangle, b: Rectangle):
    if b.y2 > a.y2 and a.x2 < b.x2 and a.y1 > b.y1 and b.x1 < a.x1:
        return False
    if a.y2 > b.y2 and b.x2 < a.x2 and b.y1 > a.y1 and b.x1 > a.x1:
        return False
    if b.y1 > a.y2 or b.x1 > a.x2 or a.y1 > b.y2 or b.x2 < a.x1:
        return False
    return True

n = int(input())
rects = [Rectangle(0, 0, 0, 0)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    rects.append(Rectangle(x1, y1, x2, y2))

parent = list(range(n + 1))

for i in range(n + 1):
    for j in range(i + 1, n + 1):
        if meet(rects[i], rects[j]):
            union(i, j)

groups = set(find(i) for i in range(n + 1))
print(len(groups) - 1)