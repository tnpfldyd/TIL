import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

numbers = list(map(int, input().split()))
segmentTree = [0] * (N * 4)

def init(x, left, right):
    if left == right:
        segmentTree[x] = numbers[left]
        return segmentTree[x]
    mid = (left + right) // 2
    leftValue = init(x * 2, left, mid)
    rightValue = init(x * 2 + 1, mid + 1, right)
    segmentTree[x] = leftValue + rightValue
    return segmentTree[x]

init(1, 0, N - 1)

def findTree(x, y, index, left, right):
    if y < left or right < x:
        return 0
    if x <= left and right <= y:
        return segmentTree[index]
    mid = (left + right) // 2
    leftValue = findTree(x, y, index * 2, left, mid)
    rightValue = findTree(x, y, index * 2 + 1, mid + 1, right)
    return leftValue + rightValue

def updateTree(target, value, x, left, right):
    if left == right == target:
        segmentTree[x] = value
        return
    if target < left or right < target:
        return
    mid = (left + right) // 2
    updateTree(target, value, x * 2, left, mid)
    updateTree(target, value, x * 2 + 1, mid + 1, right)
    segmentTree[x] = segmentTree[x * 2] + segmentTree[x * 2 + 1]

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if y < x:
        x, y = y, x
    print(findTree(x - 1, y - 1, 1, 0, N - 1))
    updateTree(a - 1, b, 1, 0, N - 1)