import sys
input = sys.stdin.readline

N = int(input())
stack = []
answer = []
cnt = 1
for _ in range(N):
    number = int(input())
    while cnt <= number:
        stack.append(cnt)
        answer.append('+')
        cnt += 1
    if stack[-1] == number:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        break
else:
    for a in answer:
        print(a)

