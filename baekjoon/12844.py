import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
segmentTree = [0] * (N * 4)
lazyTree = [0] * (N * 4)

def init(index, start, end):
    if start == end:
        segmentTree[index] = numbers[start]
        return
    
    mid = (start + end) // 2
    init(index * 2, start, mid)
    init(index * 2 + 1, mid + 1, end)
    segmentTree[index] = segmentTree[index * 2] ^ segmentTree[index * 2 + 1]
    return

def lazy(index, start, end):
    if lazyTree[index]:
        if start != end:
            lazyTree[index * 2] ^= lazyTree[index]
            lazyTree[index * 2 + 1] ^= lazyTree[index]

        if (end - start + 1) % 2:
            segmentTree[index] ^= lazyTree[index]
        lazyTree[index] = 0

def update(index, start, end, left, right, value):
    lazy(index, start, end)
    if right < start or end < left:
        return
    if left <= start and end <= right:
        lazyTree[index] ^= value
        lazy(index, start, end)
        return
    mid = (start + end) // 2
    update(index * 2, start, mid, left, right, value)
    update(index * 2 + 1, mid + 1, end, left, right, value)
    segmentTree[index] = segmentTree[index * 2] ^ segmentTree[index * 2 + 1]
    return

def query(index, start, end, left, right):
    lazy(index, start, end)
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return segmentTree[index]
    mid = (start + end) // 2
    return query(index * 2, start, mid, left, right) ^ query(index * 2 + 1, mid + 1, end, left, right)

init(1, 0, N - 1)

for _ in range(int(input())):
    a, *orders = map(int, input().split())
    if a == 1:
        i, j, k = orders
        update(1, 0, N - 1, i, j, k)
    else:
        i, j = orders
        print(query(1, 0, N - 1, i, j))