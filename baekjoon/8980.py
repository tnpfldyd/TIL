import sys

input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())

order_list = [tuple(map(int, input().split())) for _ in range(M)]

order_list.sort(key=lambda x : x[1])

truck = [0] * N
result = 0

for i in range(M):
    f, t, s = order_list[i]
    max_truck = 0
    for j in range(f, t):
        max_truck = max(max_truck, truck[j])
    
    capa = min(s, C - max_truck)
    for j in range(f, t):
        truck[j] += capa
    result += capa
print(result)