N = int(input())
A = list(map(int, input().split()))
max_previous = A[0]
sequence_length = 1
longest_sequence = 1

for i in range(1, N):
    if A[i] < max_previous:
        sequence_length += 1
        longest_sequence = max(longest_sequence, sequence_length)
    else:
        max_previous = A[i]
        sequence_length = 1

print(longest_sequence)