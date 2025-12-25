import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

bad = [0] * (N - 1)
for i in range(N - 1):
    if A[i] > A[i + 1]:
        bad[i] = 1

psum = [0] * N
for i in range(N - 1):
    psum[i + 1] = psum[i] + bad[i]

Q = int(input())
out = []

for _ in range(Q):
    x, y = map(int, input().split())
    if x == y:
        out.append("0")
    else:
        out.append(str(psum[y - 1] - psum[x - 1]))

print("\n".join(out))