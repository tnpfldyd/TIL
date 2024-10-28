import sys
from heapq import heappop, heappush

input = sys.stdin.readline

class Ardenia:
    def __init__(self, n, m):
        priority_queue = []
        lake_indices = [[] for _ in range(n + 1)]
        queries = list(map(int, input().split()))

        is_full = [True] * (n + 1)
        for i in range(m - 1, -1, -1):
            lake_indices[queries[i]].append(i)
        for i in range(1, n + 1):
            if lake_indices[i]:
                heappush(priority_queue, lake_indices[i].pop())
        
        is_possible = 'YES'
        suck_up_results = []
        for lake in queries:
            if not lake:
                if priority_queue:
                    index = heappop(priority_queue)
                    suck_up_results.append(queries[index])
                    is_full[queries[index]] = False
                else:
                    suck_up_results.append(0)
            else:
                if is_full[lake]:
                    is_possible = 'NO'
                    break
                is_full[lake] = True
                if lake_indices[lake]:
                    heappush(priority_queue, lake_indices[lake].pop())

        self.result = (is_possible, suck_up_results)

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        village = Ardenia(*map(int, input().split()))
        print(village.result[0])
        if village.result[0] == 'YES':
            print(*village.result[1])
