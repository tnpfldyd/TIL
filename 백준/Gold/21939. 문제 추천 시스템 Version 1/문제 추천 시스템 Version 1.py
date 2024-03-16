from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
max_pq, min_pq = [], []
check = {}

for _ in range(N):
    p, l = map(int, input().split())
    heappush(max_pq, (-l, -p))
    heappush(min_pq, (l, p))
    check[p] = l

M = int(input())
for _ in range(M):
    order, *args = input().split()
    if order == 'recommend':
        x = args[0]
        if x == '1':
            while max_pq and check[-max_pq[0][1]] != -max_pq[0][0]:
                heappop(max_pq)
            print(-max_pq[0][1])
        else:
            while min_pq and check[min_pq[0][1]] != min_pq[0][0]:
                heappop(min_pq)
            print(min_pq[0][1])
    elif order == 'add':
        p, l = map(int, args)
        heappush(max_pq, (-l, -p))
        heappush(min_pq, (l, p))
        check[p] = l
    else:
        p = int(args[0])
        check[p] = 0