import sys
input = sys.stdin.readline

N = int(input())
maxSize = 1000001
segmentTree = [0] * (maxSize * 4)

def query(index, start, end, target):
    if start == end:
        update(1, 1, maxSize, start, -1)
        return start
    mid = (start + end) // 2
    nextValue = segmentTree[index * 2]
    if nextValue >= target:
        return query(index * 2, start, mid, target)
    else:
        return query(index * 2 + 1, mid + 1, end, target - nextValue)

def update(index, start, end, target, value):
    if target < start or end < target:
        return
    segmentTree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(index * 2, start, mid, target, value)
    update(index * 2 + 1, mid + 1, end, target, value)
for _ in range(N):
    orders, *idx = map(int, input().split())
    if orders == 1:
        print(query(1, 1, maxSize, idx[0]))
    else:
        a, b = idx
        update(1, 1, maxSize, a, b)