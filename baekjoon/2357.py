from math import ceil, log2
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
treeSize = 1 << (ceil(log2(N)) + 1)
segmentTree = [0] * treeSize

def init(index, left, right):
    if left == right:
        segmentTree[index] = (numbers[left], numbers[left])
        return segmentTree[index]
    mid = (left + right) // 2
    leftValue = init(index * 2, left, mid)
    rightValue = init(index * 2 + 1, mid + 1, right)
    segmentTree[index] = (min(leftValue[0], rightValue[0]), max(leftValue[1], rightValue[1]))
    return segmentTree[index]

def findTree(a, b, index, left, right):
    if a > right or b < left:
        return (INF, 0)
    if a <= left and right <= b:
        return segmentTree[index]
    mid = (left + right) // 2
    leftValue = findTree(a, b, index * 2, left, mid)
    rightValue = findTree(a, b, index * 2 + 1, mid + 1, right)
    return (min(leftValue[0], rightValue[0]), max(leftValue[1], rightValue[1]))

init(1, 0, N - 1)

for _ in range(M):
    a, b = map(int, input().split())
    print(*findTree(a - 1, b - 1, 1, 0, N - 1))