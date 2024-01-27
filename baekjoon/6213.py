import sys
input = sys.stdin.readline
INF = sys.maxsize

N, Q = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
segmentTree = [0] * (N * 4)

def init(index, start, end):
    if start == end:
        value = numbers[start]
        segmentTree[index] = (value, value)
        return segmentTree[index]
    mid = (start + end) // 2
    leftValue = init(index * 2, start, mid)
    rightValue = init(index * 2 + 1, mid + 1, end)
    segmentTree[index] = (min(leftValue[0], rightValue[0]), max(leftValue[1], rightValue[1]))
    return segmentTree[index]

def query(index, start, end, left, right):
    if end < left or right < start:
        return (INF, 0)
    if left <= start and end <= right:
        return segmentTree[index]
    mid = (start + end) // 2
    leftValue = query(index * 2, start, mid, left, right)
    rightValue = query(index * 2 + 1, mid + 1, end, left, right)
    return (min(leftValue[0], rightValue[0]), max(leftValue[1], rightValue[1]))

init(1, 0, N - 1)
for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    minValue, maxValue = query(1, 0, N - 1, a, b)
    print(maxValue - minValue)