import sys
from collections import defaultdict

input = sys.stdin.readline

def count_cousins(n, k, seq):
    tree = defaultdict(list)
    rootidx = -1
    for i in range(1, len(seq)):
        if seq[i] - seq[i - 1] > 1:
            rootidx += 1
        tree[seq[rootidx]].append(seq[i])
        tree[seq[i]].append(seq[rootidx])

    if rootidx == -1:
        return 0

    if k not in tree or not tree[k]:
        return 0
    k_par = tree[k][0]
    if k_par > k:
        return 0

    if k_par not in tree or not tree[k_par]:
        return 0
    k_anc = tree[k_par][0]
    if k_anc > k_par:
        return 0

    sib = 0
    for par in tree[k_anc]:
        if par < k_anc or par == k_par:
            continue
        sib += len(tree[par][1:])

    return sib

while True:
    n, k = map(int, input().split())
    if n == 0:
        break
    seq = list(map(int, input().split()))
    print(count_cousins(n, k, seq))