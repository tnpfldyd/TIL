import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = input().split()
    a_index, b_index = [], []
    for i in range(len(A)):
        if A[i] == 'a':
            a_index.append(i)
        if B[i] == 'a':
            b_index.append(i)
    result = sum([abs(a_index[i] - b_index[i]) for i in range(len(a_index))])
    print(result)