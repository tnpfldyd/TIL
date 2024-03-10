import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
def dfs(node):
    global answer, flag, end_node
    left_node, right_node = graph[node][0], graph[node][1]
    
    if left_node != -1:
        answer += 1
        dfs(left_node)
        if flag:
            answer += 1
    if right_node != -1:
        answer += 1
        dfs(right_node)
        if flag:
            answer += 1
    if node == end_node:
        flag = False
        return

def inorder(node):
    global end_node
    left_node, right_node = graph[node][0], graph[node][1]
    
    if left_node != -1:
        inorder(left_node)
    end_node = node
    if right_node != -1:
        inorder(right_node)

end_node = 0
answer = 0
flag = True
N = int(input())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(N):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    graph[a].append(c)

inorder(1)
dfs(1)
print(answer)