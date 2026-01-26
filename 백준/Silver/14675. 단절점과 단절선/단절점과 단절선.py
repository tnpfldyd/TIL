import sys
input = sys.stdin.readline

n = int(input())
degree = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    degree[a] += 1
    degree[b] += 1

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    
    if t == 1:
        print("yes" if degree[k] >= 2 else "no")
    else:
        print("yes")