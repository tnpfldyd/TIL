N = int(input())

result = [0,1,2]
if N > 2:
    for i in range(2, N):
        result.append(result[-1] + result[-2])
print(result[N] % 10007)