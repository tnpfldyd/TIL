import sys, math
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
treeSize = 1 << (math.ceil(math.log2(N)) + 1)
segmentTree = [0] * treeSize
lazyTree = [0] * treeSize

def init(index, left, right):
    if left == right:
        segmentTree[index] = numbers[left]
        return
    mid = (left + right) // 2
    init(index * 2, left, mid)
    init(index * 2 + 1, mid + 1, right)

def updateSegmentTree(index, left, right, start, end, diff):
    if start <= left and right <= end:
        segmentTree[index] += diff
        return
    mid = (left + right) // 2
    if start <= mid: updateSegmentTree(index * 2, left, mid, start, end, diff)
    if end > mid: updateSegmentTree(index * 2 + 1, mid + 1, right, start, end, diff)

def getCurrentNode(index, left, right, target):
    if left == right: return segmentTree[index]
    mid = (left + right) // 2
    if target <= mid: return getCurrentNode(index * 2, left, mid, target) + segmentTree[index]
    elif target > mid: return getCurrentNode(index * 2 + 1, mid + 1, right, target) + segmentTree[index]
init(1, 0, N - 1)

for _ in range(int(input())):
    a, *orders = list(map(int, input().split()))
    if a == 1:
        b, c, d = orders
        updateSegmentTree(1, 0, N - 1, b - 1, c - 1, d)
    else:
        target = orders[0]
        print(getCurrentNode(1, 0, N - 1, target - 1))