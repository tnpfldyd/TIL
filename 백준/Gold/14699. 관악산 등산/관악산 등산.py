import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = 0, 0
max_height = 0
height = [0] * 5003
cache = [-1] * 5003
nodes = defaultdict(list)

def input_data():
    global N, M, max_height
    N, M = map(int, input().split())
    lines = list(map(int, input().split()))
    for i in range(1, N + 1):
        height[i] = lines[i - 1]
        max_height = max(max_height, height[i])
    for i in range(N + 1, N + 1 + M):
        from_node, to_node = map(int, input().split())
        nodes[from_node].append(to_node)
        nodes[to_node].append(from_node)

def path(index, h):
    if h == max_height or not nodes[index]:
        return 1
    if cache[index] != -1:
        return cache[index]

    ret = 1
    for neighbor in nodes[index]:
        if h < height[neighbor]:
            ret = max(ret, path(neighbor, height[neighbor]) + 1)
    cache[index] = ret
    return ret

def solution():
    for i in range(1, N + 1):
        print(path(i, height[i]))

if __name__ == "__main__":
    input_data()
    solution()