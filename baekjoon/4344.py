T = int(input())

for i in range(T):
    A = list(map(int, input().split()))
    result = []
    for j in range(1, len(A)):
        A_Average = sum(A[1::]) / A[0]
        if A[j] > A_Average:
            result.append(A[j])
    new_result = (len(result) / A[0] * 100)
    print(f'{new_result:.3f}'+'%')