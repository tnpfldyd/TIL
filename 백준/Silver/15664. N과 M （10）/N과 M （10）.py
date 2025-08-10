import sys
input = sys.stdin.readline
from collections import Counter

def backtrack(path, last_value):
    if len(path) == m:
        result.add(tuple(path))
        return
    
    for value in sorted(count.keys()):
        if value >= last_value and count[value] > 0:
            count[value] -= 1
            path.append(value)
            backtrack(path, value)
            path.pop()
            count[value] += 1

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
count = Counter(numbers)

result = set()
backtrack([], 0)

for seq in sorted(result):
    print(' '.join(map(str, seq)))