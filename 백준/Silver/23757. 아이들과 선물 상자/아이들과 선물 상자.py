import heapq
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    c = list(map(int, input().split()))
    w = list(map(int, input().split()))

    heap = [-x for x in c]
    heapq.heapify(heap)

    for need in w:
        if not heap:
            print(0)
            return
        max_gift = -heapq.heappop(heap)
        if max_gift < need:
            print(0)
            return
        remaining = max_gift - need
        if remaining > 0:
            heapq.heappush(heap, -remaining)
    
    print(1)

main()