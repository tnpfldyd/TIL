import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

top_k = heapq.nlargest(K, A)
ans = sum(top_k) - K * (K - 1) // 2

print(ans)