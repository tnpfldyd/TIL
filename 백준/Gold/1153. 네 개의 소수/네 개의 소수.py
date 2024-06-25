def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    N = int(input().strip())
    if N < 8:
        print(-1)
    else:
        if N % 2:
            print(2, 3, end=" ")
            for i in range(2, N):
                if is_prime(i) and is_prime(N - 5 - i):
                    print(i, N - 5 - i)
                    break
        else:
            print(2, 2, end=" ")
            for i in range(2, N):
                if is_prime(i) and is_prime(N - 4 - i):
                    print(i, N - 4 - i)
                    break

if __name__ == "__main__":
    main()
