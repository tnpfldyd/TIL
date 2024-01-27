import sys
input = sys.stdin.readline
MAX = 65536
N, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
segment_tree = [0] * (MAX * 4)

def update(cur, start, end, target, value):
    if start == end:
        segment_tree[cur] += value
        return
    mid = (start + end) // 2
    if target <= mid:
        update(cur * 2, start, mid, target, value)
    else:
        update(cur * 2 + 1, mid + 1, end, target, value)
    segment_tree[cur] = segment_tree[cur * 2] + segment_tree[cur * 2 + 1]

def find(cur, start, end, target):
    if start == end:
        return start
    mid = (start + end) // 2
    if target <= segment_tree[cur * 2]:
        return find(cur * 2, start, mid, target)
    else:
        return find(cur * 2 + 1, mid + 1, end, target - segment_tree[cur * 2])

left = right = 0
mid = (K + 1) // 2
result = 0

while right < K - 1:
    update(1, 0, MAX - 1, numbers[right], 1)
    right += 1

while right < N:
    update(1, 0, MAX - 1, numbers[right], 1)
    result += find(1, 0, MAX - 1, mid)
    update(1, 0, MAX - 1, numbers[left], -1)
    left += 1
    right += 1

print(result)