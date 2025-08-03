import sys
input = sys.stdin.readline

def cantor(n):
    length = 3 ** n
    s = ['-'] * length
    
    def divide(start, size, depth):
        if depth == n:
            return
        
        third = size // 3
        for i in range(start + third, start + third * 2):
            s[i] = ' '

        divide(start, third, depth + 1)
        divide(start + third * 2, third, depth + 1)
    
    divide(0, length, 0)
    return ''.join(s)

try:
    while True:
        line = input()
        if not line:
            break
        n = int(line.strip())
        print(cantor(n))
except EOFError:
    pass