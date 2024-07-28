import math
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())

graph = [[] for _ in range(N + 1)]
parent = [-1] * (N + 1)
child_count = [0] * (N + 1)
edges = []

count_d, count_g = 0, 0

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)
    edges.append([u, v])

def count_GraphTriplets(node):
    child_num = len(graph[node])
    return math.comb(child_num, 3)

for i in range(1, N + 1):
    count_g += count_GraphTriplets(i)

for u, v in edges:
    count_d += (len(graph[u]) - 1) * (len(graph[v]) - 1)

if count_d > count_g * 3:
    print("D")
elif count_d < count_g * 3:
    print("G")
else:
    print("DUDUDUNGA")
