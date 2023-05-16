from heapq import heappop, heappush

N, K = map(int, input().split())
height = list(map(int, input().split()))
diff = []

for i in range(1, N):
    heappush(diff, height[i] - height[i - 1])

answer = 0

for _ in range(N - K):
    answer += heappop(diff)

print(answer)