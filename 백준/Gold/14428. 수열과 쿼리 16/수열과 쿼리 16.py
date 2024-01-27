import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
numbers = list(map(int, input().split()))
segmentTree = [0] * (N * 4)

def init(index, left, right):
    if left == right:
        segmentTree[index] = (numbers[left], left + 1)
        return segmentTree[index]
    mid = (left + right) // 2
    leftValue = init(index * 2, left, mid)
    rightValue = init(index * 2 + 1, mid + 1, right)
    segmentTree[index] = leftValue if leftValue[0] <= rightValue[0] else rightValue
    return segmentTree[index]

def updateSegmentTree(index, left, right, target, value):
    if target < left or right < target:
        return
    if left == right == target:
        segmentTree[index] = (value, left + 1)
        return
    mid = (left + right) // 2
    updateSegmentTree(index * 2, left, mid, target, value)
    updateSegmentTree(index * 2 + 1, mid + 1, right, target, value)
    segmentTree[index] = segmentTree[index * 2] if segmentTree[index * 2][0] <= segmentTree[index * 2 + 1][0] else segmentTree[index * 2 + 1]

def getIntervalMinimumIndex(index, left, right, start, end):
    if end < left or right < start:
        return (INF, 100001)
    if start <= left and right <= end:
        return segmentTree[index]
    mid = (left + right) // 2
    leftValue = getIntervalMinimumIndex(index * 2, left, mid, start, end)
    rightValue = getIntervalMinimumIndex(index * 2 + 1, mid + 1, right, start, end)
    return leftValue if leftValue[0] <= rightValue[0] else rightValue

init(1, 0, N - 1)

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == 1:
        updateSegmentTree(1, 0, N - 1, b - 1, c)
    else:
        print(getIntervalMinimumIndex(1, 0, N - 1, b - 1, c - 1)[1])