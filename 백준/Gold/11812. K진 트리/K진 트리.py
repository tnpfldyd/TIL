import sys
input = sys.stdin.readline

def get_depth(node):
    depth, count = 0, 0
    while True:
        count += k ** depth
        if count >= node:
            return depth
        depth += 1

def get_parent(node):
    return (node - 2) // k + 1

def find_lca(node1, node2):
    depth1 = get_depth(node1)
    depth2 = get_depth(node2)
    
    while depth1 > depth2:
        node1 = get_parent(node1)
        depth1 -= 1
    
    while depth2 > depth1:
        node2 = get_parent(node2)
        depth2 -= 1
    
    while node1 != node2:
        node1 = get_parent(node1)
        node2 = get_parent(node2)
    
    return node1

n, k, q = map(int, input().split())
for _ in range(q):
    node1, node2 = map(int, input().split())
    if k == 1:
        print(abs(node1 - node2))
        continue
    print(get_depth(node1) + get_depth(node2) - 2 * get_depth(find_lca(node1, node2)))
