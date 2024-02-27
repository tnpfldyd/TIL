from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, T = map(int, input().split())
arr = [int(input()) for _ in range(N)]

def count(k):
    pq = []
    for i in range(k):
        heappush(pq, arr[i])
    
    start = k
    value = 0

    while start <= N - 1:
        cur = arr[start]
        value = heappop(pq)
        heappush(pq, cur + value)
        start += 1
    
    if pq:
        value = max(pq)
    
    return value

left, right = -1, N

while left + 1 < right:
    mid = (left + right) // 2

    if count(mid) <= T:
        right = mid
    else:
        left = mid

print(right)