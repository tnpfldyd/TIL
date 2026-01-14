import sys
input = sys.stdin.readline

N = int(input())
target = list(map(int, input().split()))

effect = [0] * (N + 3)
flip = 0
count = 0

for i in range(N):
    flip ^= effect[i]

    if flip != target[i]:
        count += 1
        flip ^= 1
        effect[i + 3] ^= 1

print(count)