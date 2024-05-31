N = int(input())
P = tuple(map(int, input().split()))
bit = result = 0
for p in P:
    bit ^= p

if not bit:
    print(0)
else:
    for i in range(N):
        if bit ^ P[i] <= P[i]:
            result += 1
    print(result)