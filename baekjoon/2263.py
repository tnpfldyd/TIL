import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
N = int(input())

in_order = [0] + list(map(int, input().split()))
in_idx = [0] * (N + 1)
for i in range(1, N + 1):
    in_idx[in_order[i]] = i
post_order = [0] + list(map(int, input().split()))

def get_preorder(ins, ine, pos, poe):
    if ins > ine or pos > poe:
        return
    root = in_idx[post_order[poe]]
    left = root - ins
    print(in_order[root], end=' ')
    get_preorder(ins, root - 1, pos, pos + left - 1)
    get_preorder(root + 1, ine, pos + left, poe - 1)

get_preorder(1, N, 1, N)