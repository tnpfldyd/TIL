def backtrack(arr, sequence, M):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for num in arr:
        sequence.append(num)
        backtrack(arr, sequence, M)
        sequence.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
backtrack(arr, [], M)