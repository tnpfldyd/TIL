from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline

T = int(input())
MOD = 1000000007
for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    heapify(numbers)
    answer = 1
    while len(numbers) > 1:
        x, y = heappop(numbers), heappop(numbers)
        cur = x * y
        heappush(numbers, cur)
        answer = answer * (cur % MOD) % MOD
    print(answer)