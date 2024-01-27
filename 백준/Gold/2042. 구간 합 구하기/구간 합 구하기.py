import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())
numbers = [int(input()) for _ in range(N)]
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

def findTree(b, c, x, left, right):
    if c < left or right < b:
        return 0
    if b <= left and right <= c:
        return segmentTree[x]
    mid = (left + right) // 2
    leftValue = findTree(b, c, x * 2, left, mid)
    rightValue = findTree(b, c, x * 2 + 1, mid + 1, right)
    return leftValue + rightValue

def updateTree(x, index, value, left, right):
    if left == right == index:
        segmentTree[x] = value
        return
    if index < left or right < index:
        return
    mid = (left + right) // 2
    updateTree(x * 2, index, value, left, mid)
    updateTree(x * 2 + 1, index, value, mid + 1, right)
    segmentTree[x] = segmentTree[x * 2] + segmentTree[x * 2 + 1]

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        updateTree(1, b - 1, c, 0, N - 1)
    else:
        print(findTree(b -  1, c - 1, 1, 0, N - 1))