def backtrack(arr, sequence, M, start):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    prev = -1
    for i in range(start, len(arr)):
        if arr[i] != prev:
            sequence.append(arr[i])
            backtrack(arr, sequence, M, i)
            sequence.pop()
            prev = arr[i]

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
backtrack(arr, [], M, 0)