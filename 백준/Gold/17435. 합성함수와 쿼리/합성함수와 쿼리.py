import sys
input = sys.stdin.readline

m = int(input())
f = list(map(int, input().split()))
f = [x - 1 for x in f]

LOG = 20
dp = [[0] * m for _ in range(LOG)]

for i in range(m):
    dp[0][i] = f[i]

for k in range(1, LOG):
    for i in range(m):
        dp[k][i] = dp[k-1][dp[k-1][i]]

Q = int(input())
output_lines = []
for _ in range(Q):
    n, x = map(int, input().split())
    current = x - 1
    bit = 0
    while n:
        if n & 1:
            current = dp[bit][current]
        n //= 2
        bit += 1
    output_lines.append(str(current + 1))

print("\n".join(output_lines))