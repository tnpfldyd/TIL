import sys
input = sys.stdin.readline

def converter(x):
    if not x: return 0
    else: return -1 if x < 0 else 1

def init(index, left, right):
    if left == right:
        segmentTree[index] = converter(numbers[left])
        return segmentTree[index]
    mid = (left + right) // 2
    segmentTree[index] = init(index * 2, left, mid) * init(index * 2 + 1, mid + 1, right)
    return segmentTree[index]

def update(index, left, right, target, value):
    if target < left or right < target:
        return
    elif left == right:
        segmentTree[index] = value
        return
    mid = (left + right) // 2
    update(index * 2, left, mid, target, value)
    update(index * 2 + 1, mid + 1, right, target, value)
    segmentTree[index] = segmentTree[index * 2] * segmentTree[index * 2 + 1]

def query(index, left, right, start, end):
    if end < left or right < start:
        return 1
    if start <= left and right <= end:
        return segmentTree[index]
    mid = (left + right) // 2
    return query(index * 2, left, mid, start, end) * query(index * 2 + 1, mid + 1, right, start, end)

while True:
    try:
        N, K = map(int, input().split())
        numbers = list(map(int, input().split()))
        segmentTree = [0] * (N * 4)
        init(1, 0, N - 1)

        for _ in range(K):
            order, a, b = input().split()
            a, b = int(a), int(b)
            if order == 'C':
                update(1, 0, N - 1, a - 1, converter(b))
            else:
                result = query(1, 0, N - 1, a - 1, b - 1)
                if result:
                    result = '-' if result < 0 else '+'
                print(result, end='')
        print()

    except Exception:
        break