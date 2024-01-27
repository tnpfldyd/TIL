import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(lambda x : int(x) % 2, input().split()))
segmentTree = [0] * (N * 4)

def init(index, left, right):
    if left == right:
        segmentTree[index] = numbers[left]
        return segmentTree[index]
    mid = (left + right) // 2
    segmentTree[index] = init(index * 2, left, mid) + init(index * 2 + 1, mid + 1, right)
    return segmentTree[index]
init(1, 0, N - 1)

def updateSegmentTree(index, left, right, target, value):
    if target < left or right < target:
        return
    if left == right:
        segmentTree[index] = value
        return
    mid = (left + right) // 2
    updateSegmentTree(index * 2, left, mid, target, value)
    updateSegmentTree(index * 2 + 1, mid + 1, right, target, value)
    segmentTree[index] = segmentTree[index * 2] + segmentTree[index * 2 + 1]

def query(index, left, right, start, end):
    if end < left or right < start:
        return 0
    if start <= left and right <= end:
        return segmentTree[index]
    mid = (left + right) // 2
    return query(index * 2, left, mid, start, end) + query(index * 2 + 1, mid + 1, right, start, end)
Q = int(input())
for _ in range(Q):
    a, b, c = map(int, input().split())
    if a == 1:
        x = c % 2
        if numbers[b - 1] != x: updateSegmentTree(1, 0, N - 1, b - 1, x)
        numbers[b - 1] = x
    elif a == 2:
        print(c - b - query(1, 0, N - 1, b - 1, c - 1) + 1)
    else:
        print(query(1, 0, N - 1, b - 1, c - 1))