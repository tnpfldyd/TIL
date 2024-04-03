memo = {}

def sequence(n):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 1
    else:
        memo[n] = sequence(n // P - X) + sequence(n // Q - Y)
        return memo[n]

N, P, Q, X, Y = map(int, input().split())

print(sequence(N))