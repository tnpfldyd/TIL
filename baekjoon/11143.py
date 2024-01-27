import sys
input = sys.stdin.readline

def getPrefixSum(index, left, right, a, b):
    if a > right or b < left:
        return 0
    if a <= left and right <= b:
        return segmentTree[index]
    mid = (left + right) // 2
    leftValue = getPrefixSum(index * 2, left, mid, a, b)
    rightValue = getPrefixSum(index * 2 + 1, mid + 1, right, a, b)
    return leftValue + rightValue

def updateSegmentTree(index, left, right, target, value):
    if target < left or right < target:
        return
    
    segmentTree[index] += value
    if left < right:
        mid = (left + right) // 2
        updateSegmentTree(index * 2, left, mid, target, value)
        updateSegmentTree(index * 2 + 1, mid + 1, right, target, value)

for _ in range(int(input())):
    B, P, Q = map(int, input().split())
    segmentTree = [0] * (B * 4)
    for _ in range(P + Q):
        order, i, j = input().split()
        i, j = map(int, [i, j])
        if order == 'P':
            updateSegmentTree(1, 1, B, i, j)
        else:
            print(getPrefixSum(1, 1, B, i, j))