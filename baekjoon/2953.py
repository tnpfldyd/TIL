result = []
for i in range(5):
    A = list(map(int,input().split()))
    B = sum(A)
    result.append(B)
tmp = max(result)
idx = result.index(tmp)
print(idx+1, tmp)