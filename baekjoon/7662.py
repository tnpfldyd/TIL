from heapq import heappop, heappush
import sys
input = sys.stdin.readline

T = int(input())

def pq_pop(pq):
    while pq and visited[pq[0][1]]:
        heappop(pq)

for _ in range(T):
    min_pq = []
    max_pq = []
    K = int(input())
    visited = [False] * K
    for i in range(K):
        order, num = input().split()
        num = int(num)
        if order == 'I':
            heappush(min_pq, (num, i))
            heappush(max_pq, (-num, i))
        else:
            if num == -1:
                pq_pop(min_pq)
                if min_pq:
                    visited[heappop(min_pq)[1]] = True
            elif num == 1:
                pq_pop(max_pq)
                if max_pq:
                    visited[heappop(max_pq)[1]] = True

    pq_pop(min_pq); pq_pop(max_pq)

    if not min_pq:
        print('EMPTY')
    else:
        print(-max_pq[0][0], min_pq[0][0])