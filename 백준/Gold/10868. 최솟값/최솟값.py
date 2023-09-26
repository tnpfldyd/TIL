import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())

segmentTree = [0] * (N * 4)
numbers = [int(input()) for _ in range(N)]

def init(x, left, right):
    if left == right:
        segmentTree[x] = numbers[left]
        return segmentTree[x]
    mid = (left + right) // 2
    leftValue = init(x * 2, left, mid)
    rightValue = init(x * 2 + 1, mid + 1, right)
    segmentTree[x] = min(leftValue, rightValue)
    return segmentTree[x]

def findTree(a, b, x, left, right):
    if b < left or right < a:
        return INF
    if a <= left and right <= b:
        return segmentTree[x]
    mid = (left + right) // 2
    leftValue = findTree(a, b, x * 2, left, mid)
    rightValue = findTree(a, b, x * 2 + 1, mid + 1, right)
    return min(leftValue, rightValue)

init(1, 0, N - 1)
for _ in range(M):
    a, b = map(int, input().split())
    print(findTree(a - 1, b - 1, 1, 0, N - 1))
