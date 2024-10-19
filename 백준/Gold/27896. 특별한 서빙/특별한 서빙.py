import sys
import heapq

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    pq = []
    total_sum = 0
    answer = 0
    numbers = list(map(int, input().split()))
    for number in numbers:
        heapq.heappush(pq, -number)
        total_sum += number
        
        while total_sum >= M:
            answer += 1
            total_sum += heapq.heappop(pq) * 2

    print(answer)

if __name__ == "__main__":
    main()
