from heapq import heappop, heappush
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    K = int(input())
    ans = 0
    pq = []
    nums = list(map(int, input().split()))
    for i in range(K):
        heappush(pq, nums[i])

    while len(pq) > 1:
        first = heappop(pq)
        second = heappop(pq)
        ans += first + second
        heappush(pq, first + second)
    print(ans)