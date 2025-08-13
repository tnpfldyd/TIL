def backtrack(arr, sequence, M):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    prev = -1
    for num in arr:
        if num != prev:
            sequence.append(num)
            backtrack(arr, sequence, M)
            sequence.pop()
            prev = num

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
backtrack(arr, [], M)