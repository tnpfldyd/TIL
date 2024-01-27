import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
segmentTree = [0] * (N * 4)
lazyTree = [0] * (N * 4)

def init(index, left, right):
    if left == right:
        segmentTree[index] = numbers[left]
        return segmentTree[index]
    mid = (left + right) // 2
    leftValue = init(index * 2, left, mid)
    rightValue = init(index * 2 + 1, mid + 1, right)
    segmentTree[index] = leftValue + rightValue
    return segmentTree[index]

def updateLazyTree(index, left, right):
    if lazyTree[index]:
        if left != right:
            lazyTree[index * 2] += lazyTree[index]
            lazyTree[index * 2 + 1] += lazyTree[index]
        segmentTree[index] += lazyTree[index] * (right - left + 1)
        lazyTree[index] = 0

def updateSegmentTree(index, left, right, start, end, diff):
    updateLazyTree(index, left, right)
    if start > right or end < left:
        return
    if start <= left and right <= end:
        lazyTree[index] = diff
        updateLazyTree(index, left, right)
        return
    mid = (left + right) // 2
    updateSegmentTree(index * 2, left, mid, start, end, diff)
    updateSegmentTree(index * 2 + 1, mid + 1, right, start, end, diff)
    segmentTree[index] = segmentTree[index * 2] + segmentTree[index * 2 + 1]

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

init(1, 0, N - 1)

for _ in range(M + K):
    a, *orders = list(map(int, input().split()))
    if a == 1:
        b, c, d = orders
        updateSegmentTree(1, 0, N - 1, b - 1, c - 1, d)
    else:
        b, c = orders
        print(getPrefixSum(1, 0, N - 1, b - 1, c - 1))