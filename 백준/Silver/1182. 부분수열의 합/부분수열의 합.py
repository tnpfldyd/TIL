import itertools
n, m = map(int, input().split())
data = list(map(int, input().strip().split()))
cnt = 0
for i in range(1, n+1):
    for j in itertools.combinations(data, i):
        if sum(j) == m:
            cnt += 1
print(cnt)