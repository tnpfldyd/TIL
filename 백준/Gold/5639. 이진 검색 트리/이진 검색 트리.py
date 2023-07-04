import sys
sys.setrecursionlimit(10 ** 6)
def dfs(s, e):
    if s >= e:
        return
    if s == e - 1:
        print(tree[s])
        return

    idx = s + 1
    while idx < e:
        if tree[s] < tree[idx]:
            break
        idx += 1

    dfs(s + 1, idx)
    dfs(idx, e)
    print(tree[s])

tree = []
for line in sys.stdin:
    num = int(line)
    tree.append(num)

dfs(0, len(tree))