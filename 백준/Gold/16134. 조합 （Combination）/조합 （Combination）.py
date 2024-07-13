N, R = map(int, input().split())

p = 1000000007

num = 1
for i in range(N - R + 1, N + 1):
    num = (num * i) % p

den = 1
for i in range(1, R + 1):
    den = (den * i) % p

inv = p - 2
res = 1
while inv > 0:
    if inv % 2 == 1:
        res = (res * den) % p
    den = (den * den) % p
    inv //= 2

print((num * res) % p)
