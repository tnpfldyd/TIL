import sys
input = sys.stdin.readline
N, M = map(int, input().split())

segmentTree = [0] * (N * 4)

def getPrefixSum(a, b, index, left, right):
    if a > right or b < left:
        return 0
    if a <= left and right <= b:
        return segmentTree[index]
    mid = (left + right) // 2
    leftValue = getPrefixSum(a, b, index * 2, left, mid)
    rightValue = getPrefixSum(a, b, index * 2 + 1, mid + 1, right)
    return leftValue + rightValue

def updateSegmentTree(target, value, index, left, right):
    if left == right == target:
        segmentTree[index] = value
        return
    if target < left or right < target:
        return
    mid = (left + right) // 2
    updateSegmentTree(target, value, index * 2, left, mid)
    updateSegmentTree(target, value, index * 2 + 1, mid + 1, right)
    segmentTree[index] = segmentTree[index * 2] + segmentTree[index * 2 + 1]
for _ in range(M):
    order, a, b = map(int, input().split())
    if not order:
        if a > b:
            a, b = b, a
        print(getPrefixSum(a - 1, b - 1, 1, 0, N - 1))
    else:
        updateSegmentTree(a - 1, b, 1, 0, N - 1)