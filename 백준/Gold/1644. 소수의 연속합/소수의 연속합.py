def get_primes(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes

N = int(input())
primes = get_primes(N) + [0]
left = right = answer = 0
total = primes[0]

while left <= right and right < len(primes) - 1:
    if total > N:
        total -= primes[left]
        left += 1
    else:
        if total == N:
            answer += 1
        right += 1
        total += primes[right]
print(answer)