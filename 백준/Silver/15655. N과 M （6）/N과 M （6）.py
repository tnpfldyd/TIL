def backtrack(start, path):
    if len(path) == m:
        print(' '.join(map(str, path)))
        return
    
    for i in range(start, n):
        path.append(numbers[i])
        backtrack(i + 1, path)
        path.pop()

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

backtrack(0, [])