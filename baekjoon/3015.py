import sys
input = sys.stdin.readline

N = int(input())
result = 0
stack = []

for _ in range(N):
    height = int(input())

    # 큰 키
    while stack and height > stack[-1][0]:
        result += stack[-1][1]
        stack.pop()

    # 비어있음
    if not stack:
        stack.append((height, 1))

    else:
        # 같은 키
        if stack[-1][0] == height:
            cur = stack[-1][1]
            stack.pop()
            if stack:
                result += 1
            result += cur
            stack.append((height, cur+1))
        # 작은 키
        else:
            result += 1
            stack.append((height, 1))

print(result)