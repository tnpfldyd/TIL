T = int(input())
for i in range(T):
    A = input().split()
    result = []
    for j in A[1]:
        result.append(j)
    del result[int(A[0])-1]
    for k in result:
        print(k, end='')
    print()