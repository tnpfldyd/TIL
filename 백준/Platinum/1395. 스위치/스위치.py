import sys
input = sys.stdin.readline
N, M = map(int, input().split())
segmentTree = [0] * (N * 4)
lazyTree = [0] * (N * 4)

def updateLazyTree(index, left, right):
    if lazyTree[index] % 2:
        if left != right:
            lazyTree[index * 2] += lazyTree[index]
            lazyTree[index * 2 + 1] += lazyTree[index]
        segmentTree[index] = (right - left + 1) - segmentTree[index]
        lazyTree[index] = 0

def updateSegmentTree(index, left, right, start, end):
    updateLazyTree(index, left, right)
    if end < left or right < start:
        return
    if start <= left and right <= end:
        lazyTree[index] = 1
        updateLazyTree(index, left, right)
        return
    mid = (left + right) // 2
    updateSegmentTree(index * 2, left, mid, start, end)
    updateSegmentTree(index * 2 + 1, mid + 1, right, start, end)
    segmentTree[index] = segmentTree[index * 2] + segmentTree[index * 2 + 1]

def query(index, left, right, start, end):
    updateLazyTree(index, left, right)
    if end < left or right < start:
        return 0
    if start <= left and right <= end:
        return segmentTree[index]
    mid = (left + right) // 2
    return query(index * 2, left, mid, start, end) + query(index * 2 + 1, mid + 1, right, start, end)

for _ in range(M):
    a, b, c = map(int, input().split())
    b -= 1; c -= 1
    if not a:
        updateSegmentTree(1, 0, N - 1, b, c)
    else:
        print(query(1, 0, N - 1, b, c))