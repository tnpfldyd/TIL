import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()
min_add = 5

for i in range(N):
    for j in range(i, N):
        start = arr[i]
        end = arr[j]
        
        if end - start > 4:
            break
        
        existing = set()
        for k in range(i, j + 1):
            existing.add(arr[k])
        
        needed = 0
        for num in range(start, start + 5):
            if num not in existing:
                needed += 1
        
        min_add = min(min_add, needed)

print(min_add)