import sys
from collections import Counter

input = sys.stdin.readline
tree_counts = Counter()
total_trees = 0

try:
    while True:
        tree = input().strip()
        if not tree and total_trees > 0:
            break
        tree_counts[tree] += 1
        total_trees += 1
except EOFError:
    pass

if total_trees > 0:
    tree_names = sorted(tree_counts.keys())
    for tree in tree_names:
        percentage = (tree_counts[tree] / total_trees) * 100
        print(f"{tree} {percentage:.4f}")