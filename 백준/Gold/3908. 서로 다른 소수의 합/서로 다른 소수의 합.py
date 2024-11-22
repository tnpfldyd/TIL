def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def main():
    T = int(input())
    primes = generate_primes(1120)

    for _ in range(T):
        n, k = map(int, input().split())
        dp = [[0] * (15) for _ in range(1121)]

        for prime in primes:
            if prime > n:
                break
            for i in range(n, 1, -1):
                if i - prime < 0:
                    continue
                if i == prime:
                    dp[i][1] = 1
                    continue
                for l in range(2, k + 1):
                    dp[i][l] += dp[i - prime][l - 1]

        print(dp[n][k])

if __name__ == "__main__":
    main()