T = int(input())
A = list(map(int, input().split()))
result = []
cnt = 0
for i in range(1, T):
    if A[i] > A[i-1]:
        cnt += A[i] - A[i-1]
        if i+1 == T:
            result.append(cnt)
    else:
        result.append(cnt)
        cnt = 0  
print(max(result))