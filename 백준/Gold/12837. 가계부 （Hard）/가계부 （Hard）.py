import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
segmentTree = [0] * (N * 4)
lazyTree = [0] * (N * 4)
def updateLazyTree(index, left, right):
    if lazyTree[index]:
        if left != right:
            lazyTree[index * 2] += lazyTree[index]
            lazyTree[index * 2 + 1] += lazyTree[index]
        segmentTree[index] += lazyTree[index] * (right - left + 1)
        lazyTree[index] = 0

def updateSegmentTree(index, left, right, target, value):
    updateLazyTree(index, left, right)
    if target < left or right < target:
        return
    if target <= left and right <= target:
        lazyTree[index] = value
        updateLazyTree(index, left, right)
        return
    mid = (left + right) // 2
    if target <= mid: updateSegmentTree(index * 2, left, mid, target, value)
    if target > mid: updateSegmentTree(index * 2 + 1, mid + 1, right, target, value)
    segmentTree[index] = segmentTree[index * 2] + segmentTree[index * 2 + 1]
    return

def getPrefixSum(index, left, right, start, end):
    updateLazyTree(index, left, right)
    if start > right or end < left:
        return 0
    if start <= left and right <= end:
        return segmentTree[index]
    mid = (left + right) // 2
    leftValue = getPrefixSum(index * 2, left, mid, start, end)
    rightValue = getPrefixSum(index * 2 + 1, mid + 1, right, start, end)
    return leftValue + rightValue

for _ in range(Q):
    a, b, c = map(int, input().split())
    if a == 1:
        updateSegmentTree(1, 0, N - 1, b - 1, c)
    else:
        print(getPrefixSum(1, 0, N - 1, b - 1, c - 1))