N, Target = map(int, input().split())
result = 0
card = list(map(int, input().split()))
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if result <= card[i]+card[j]+card[k] <= Target:
                result = card[i]+card[j]+card[k]
print(result)
