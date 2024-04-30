import sys, bisect
input = sys.stdin.readline
N = int(input())
numbers = [int(input()) for _ in range(N)]

def get_lis(s, flag):
    stack = []
    for j in range(s, N):
        cur = numbers[j] if not flag else -numbers[j]
        w = numbers[s] if not flag else -numbers[s]
        if w > cur:
            continue
        if not stack:
            stack.append(cur)
            continue
        if stack[-1] < cur:
            stack.append(cur)
        else:
            idx = bisect.bisect_left(stack, cur)
            stack[idx] = cur
    return len(stack)

result = 0
for i in range(N):
    a, b = get_lis(i, True), get_lis(i, False)
    result = max(result, a + b - 1)
    
print(result)