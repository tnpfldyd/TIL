import heapq, sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        k = int(input())
        max_heap = []
        min_heap = []
        for _ in range(k):
            operation, n = input().split()
            n = int(n)
            if operation == "I":
                heapq.heappush(max_heap, n)
                heapq.heappush(min_heap, -n)
            elif operation == "D":
                if len(max_heap) > 0 and n == 1:
                    heapq.heappop(max_heap)
                elif len(min_heap) > 0 and n == -1:
                    heapq.heappop(min_heap)

        if len(max_heap) == 0 and len(min_heap) == 0:
            print("EMPTY")
        else:
            print(max_heap[0], -min_heap[0])


if __name__ == "__main__":
    main()