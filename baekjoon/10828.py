import sys
input = sys.stdin.readline
T = int(input())
result = []
for i in range(T):
    cmd = input().rstrip().split()
    if cmd[0] == 'push':
        result.append(cmd[1])
    elif cmd[0] == 'pop':
        print(-1 if not result else result.pop())
    elif cmd[0] == 'size':
        print(len(result))
    elif cmd[0] == 'empty':
        print(0 if result else 1)
    else:
        print(-1 if not result else result[-1])
