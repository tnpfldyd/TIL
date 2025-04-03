import sys
input = sys.stdin.readline
def run_program(cmds, val):
    stack = [val]
    for cmd in cmds:
        if cmd[0] == "NUM":
            stack.append(int(cmd[1]))
        elif cmd[0] == "POP":
            if not stack: return "ERROR"
            stack.pop()
        elif cmd[0] == "INV":
            if not stack: return "ERROR"
            stack[-1] = -stack[-1]
        elif cmd[0] == "DUP":
            if not stack: return "ERROR"
            stack.append(stack[-1])
        elif cmd[0] == "SWP":
            if len(stack) < 2: return "ERROR"
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif cmd[0] == "ADD":
            if len(stack) < 2: return "ERROR"
            a = stack.pop(); b = stack.pop()
            res = a + b
            if abs(res) > 10**9: return "ERROR"
            stack.append(res)
        elif cmd[0] == "SUB":
            if len(stack) < 2: return "ERROR"
            a = stack.pop(); b = stack.pop()
            res = b - a
            if abs(res) > 10**9: return "ERROR"
            stack.append(res)
        elif cmd[0] == "MUL":
            if len(stack) < 2: return "ERROR"
            a = stack.pop(); b = stack.pop()
            res = a * b
            if abs(res) > 10**9: return "ERROR"
            stack.append(res)
        elif cmd[0] == "DIV":
            if len(stack) < 2: return "ERROR"
            a = stack.pop(); b = stack.pop()
            if a == 0: return "ERROR"
            res = abs(b) // abs(a)
            if (b < 0) ^ (a < 0): res = -res
            if abs(res) > 10**9: return "ERROR"
            stack.append(res)
        elif cmd[0] == "MOD":
            if len(stack) < 2: return "ERROR"
            a = stack.pop(); b = stack.pop()
            if a == 0: return "ERROR"
            res = abs(b) % abs(a)
            if b < 0: res = -res
            if abs(res) > 10**9: return "ERROR"
            stack.append(res)
    return stack[0] if len(stack) == 1 else "ERROR"
while True:
    cmds = []
    while True:
        line = input().strip()
        if not line: continue
        if line == "QUIT":
            sys.exit()
        if line == "END":
            break
        cmds.append(line.split())
    n = int(input().strip())
    for _ in range(n):
        v = int(input().strip())
        print(run_program(cmds, v))
    print()
    input()