import heapq

k, n = map(int, input().split())
primes = list(map(int, input().split()))

pq = []
for prime in primes:
    heapq.heappush(pq, prime)

result = 0
for i in range(n):
    result = heapq.heappop(pq)
    for j in range(k):
        value = result * primes[j]
        heapq.heappush(pq, value)
        if result % primes[j] == 0:
            break

print(result)