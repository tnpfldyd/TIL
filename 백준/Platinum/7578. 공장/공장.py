import sys
input = sys.stdin.readline

N = int(input())
A = input().split()
indexMap = {cost : idx for idx, cost in enumerate(input().split())}
segementTree = [0] * (N * 4)

def query(index, left, right, start, end):
    if end < left or right < start:
        return 0
    if start <= left and right <= end:
        return segementTree[index]
    mid = (left + right) // 2
    return query(index * 2, left, mid, start, end) + query(index * 2 + 1, mid + 1, right, start, end)

def update(index, left, right, target):
    if target < left or right < target:
        return
    if left == right:
        segementTree[index] = 1
        return
    
    mid = (left + right) // 2
    if target <= mid:
        update(index * 2, left, mid, target)
    else:
        update(index * 2 + 1, mid + 1, right, target)
    segementTree[index] = segementTree[index * 2] + segementTree[index * 2 + 1]

answer = 0
for num in A:
    idx = indexMap[num]
    answer += query(1, 0, N - 1, idx, N - 1)
    update(1, 0, N - 1, idx)

print(answer)