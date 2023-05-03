from heapq import heappop, heappush
import sys, math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    min_q = []
    max_q = []
    mid = 0
    answer = []
    N = int(input())
    N = math.ceil(N / 10)
    for i in range(N):
        for idx, num in enumerate(map(int, input().split())):
            if not i and not idx:
                mid = num
            else:
                if mid > num:
                    heappush(min_q, -num)
                else:
                    heappush(max_q, num)
            if not idx % 2:
                while len(min_q) > len(max_q):
                    heappush(max_q, mid)
                    mid = -heappop(min_q)
                while len(min_q) < len(max_q):
                    heappush(min_q, -mid)
                    mid = heappop(max_q)
                answer.append(mid)
    print(len(answer))
    for idx, num in enumerate(answer):
        if idx != 0 and not idx % 10:
            print()
        print(num, end=' ')
    print()