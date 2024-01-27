import sys
input = sys.stdin.readline

N = int(input())
numbers = sorted([(x, i) for i, x in enumerate(list(map(int, input().split())))])
segmentTree = [0] * (N * 4)

answer = 0

def query(index, left, right, start, end):
    if end < left or right < start:
        return 0
    if start <= left and right <= end:
        return segmentTree[index]
    mid = (left + right) // 2
    return query(index * 2, left, mid, start, end) + query(index * 2 + 1, mid + 1, right, start, end)

def update(index, left, right, target):
    if left == right:
        segmentTree[index] = 1
        return
    mid = (left + right) // 2
    if target <= mid:
        update(index * 2, left, mid, target)
    else:
        update(index * 2 + 1, mid + 1, right, target)
    segmentTree[index] = segmentTree[index * 2] + segmentTree[index * 2 + 1]

for i in range(N):
    answer += query(1, 0, N - 1, numbers[i][1] + 1, N - 1)
    update(1, 0, N - 1, numbers[i][1])

print( answer)