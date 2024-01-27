N, L, R, X = map(int, input().split())
score = list(map(int, input().split()))
result = 0

for i in range(1, 1<<N):
    temp = [score[j] for j in range(N) if (i & 1<<j)]
    if L <= sum(temp) <= R and max(temp) - min(temp) >= X:
        result += 1

print(result)