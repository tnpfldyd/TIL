import sys
input = sys.stdin.readline

K = int(input())
buildings = list(map(int, input().split()))

tree = [[0] * (2 ** K) for _ in range(K)]
idx = 0

def inorder(level, left, right):
    global idx
    
    if level == K:
        return
    
    mid = (left + right) // 2
    
    inorder(level + 1, left, mid - 1)
    tree[level][mid] = buildings[idx]
    idx += 1
    inorder(level + 1, mid + 1, right)

inorder(0, 0, 2 ** K - 1)

for level in range(K):
    row = [x for x in tree[level] if x != 0]
    print(*row)