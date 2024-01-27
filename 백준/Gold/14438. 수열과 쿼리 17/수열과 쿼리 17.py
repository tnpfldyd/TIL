import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
segmentTree = [0] * (N * 4)

def processSegmentTree(index, left, right, a, b, queryFunction):
    mid = (left + right) // 2
    leftValue = queryFunction(index * 2, left, mid, a, b)
    rightValue = queryFunction(index * 2 + 1, mid + 1, right, a, b)
    return min(leftValue, rightValue)

def init(index, left, right, _ = None, __ = None):
    if left == right:
        segmentTree[index] = numbers[left]
        return segmentTree[index]
    segmentTree[index] = processSegmentTree(index, left, right, _, __, init)
    return segmentTree[index]

def getMinimumValue(index, left, right, start, end):
    if start > right or end < left:
        return INF
    if start <= left and right <= end:
        return segmentTree[index]
    return processSegmentTree(index, left, right, start, end, getMinimumValue)
  
def updateSegmentTree(index, left, right, target, value):
    if left == right == target:
        segmentTree[index] = value
        return 0
    if target < left or right < target:
        return 0
    processSegmentTree(index, left, right, target, value, updateSegmentTree)
    segmentTree[index] = min(segmentTree[index * 2], segmentTree[index * 2 + 1])
    return 0

init(1, 0, N - 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        updateSegmentTree(1, 0, N - 1, b - 1, c)
    else:
        print(getMinimumValue(1, 0, N - 1, b - 1, c - 1))