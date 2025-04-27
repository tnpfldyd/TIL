import sys
input = sys.stdin.readline

n = int(input())
maps = list(map(int, input().split()))
count = [0] * n
what = [0] * n

def solve(is_right):
    stack = [(100001, 0)]
    idxs = range(n - 1, -1, -1) if is_right else range(n)
    for i in idxs:
        while stack and maps[i] >= stack[-1][0]:
            stack.pop()
        if stack:
            count[i] += len(stack) - 1
            next_idx = stack[-1][1]
            if is_right:
                if count[i]:
                    if what[i] and next_idx:
                        if abs(i + 1 - what[i]) > abs(next_idx - i - 1):
                            what[i] = next_idx
                    elif next_idx:
                        what[i] = next_idx
            else:
                what[i] = next_idx
        stack.append((maps[i], i + 1))

solve(False)
solve(True)

for i in range(n):
    if count[i]:
        print(count[i], what[i])
    else:
        print(0)