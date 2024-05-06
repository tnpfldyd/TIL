import sys
input = sys.stdin.readline
N, K = map(int, input().split())

prefix_sum = [0] * N
temp = 0
for i in range(N):
    a, b = map(int, input().split())
    if i:
        prefix_sum[i] = prefix_sum[i - 1] + max(0, a - temp)
    temp = max(temp, b)
    
orders = [1] + list(map(int, input().split()))
result = 0
for i in range(K):
    s, e = min(orders[i], orders[i + 1]), max(orders[i], orders[i + 1])
    s -= 1; e -= 1
    result += prefix_sum[e] - prefix_sum[s]
    
print(result)