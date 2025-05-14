N = int(input())
A = list(map(int, input().split()))

indexed_A = sorted((value, i) for i, value in enumerate(A))

P = [0] * N
for new_index, (_, original_index) in enumerate(indexed_A):
    P[original_index] = new_index

print(' '.join(map(str, P)))