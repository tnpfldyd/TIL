import sys
input = sys.stdin.readline

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

def check(stack, ary, p, e):
    c = [0] * len(ary)
    left = right = 0
    
    for i in range(p):
        c[stack[i]] = ary[stack[i]].left
        left += c[stack[i]]
        right += ary[stack[i]].right
    
    if left <= e <= right:
        for i in range(len(ary)):
            if c[i]:
                gap = ary[i].right - ary[i].left
                if left + gap < e:
                    left += gap
                    c[i] += gap
                else:
                    c[i] += e - left
                    print(' '.join(map(str, c)))
                    return True
    return False

def dfs(cur, n, p, stack, ary):
    if len(stack) == p:
        return check(stack, ary, p, e)
    elif cur < n:
        for i in range(stack[-1] + 1 if stack else 0, n - (p - len(stack)) + 1):
            stack.append(i)
            if dfs(cur + 1, n, p, stack, ary):
                return True
            stack.pop()
    return False

n, p, e = map(int, input().split())
ary = [Node(*map(int, input().split())) for _ in range(n)]
stack = []

if not dfs(0, n, p, stack, ary):
    print("-1")
