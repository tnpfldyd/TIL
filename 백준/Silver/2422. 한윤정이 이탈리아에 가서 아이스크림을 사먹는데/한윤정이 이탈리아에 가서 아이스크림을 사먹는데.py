import sys
input = sys.stdin.readline

N, M = map(int, input().split())

bad_pairs = set()
for _ in range(M):
    a, b = map(int, input().split())
    bad_pairs.add((min(a, b), max(a, b)))

count = 0
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        for k in range(j + 1, N + 1):
            if (i, j) not in bad_pairs and (i, k) not in bad_pairs and (j, k) not in bad_pairs:
                count += 1

print(count)