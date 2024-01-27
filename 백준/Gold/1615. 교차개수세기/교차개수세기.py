import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N + 1)]
segmentTree = [0] * ((N + 1) * 4)

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)


def query(left, right, index = 1, start = 1, end = N):
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return segmentTree[index]
    
    mid = (start + end) // 2
    return query(left, right, index * 2, start, mid) + query(left, right, index * 2 + 1, mid + 1, end)

def update(left, right, index = 1, start = 1, end = N):
    if end < left or right < start:
        return
    if left <= start and end <= right:
        segmentTree[index] += 1
        return
    mid = (start + end) // 2
    update(left, right, index * 2, start, mid)
    update(left, right, index * 2 + 1, mid + 1, end)
    segmentTree[index] = segmentTree[index * 2] + segmentTree[index * 2 + 1]

answer = 0
for i in range(1, N + 1):
    for b in matrix[i]:
        answer += query(b + 1, N)
    for b in matrix[i]:
        update(b, b)

print(answer)