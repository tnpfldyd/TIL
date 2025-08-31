import sys
input = sys.stdin.readline

P = int(input())

for _ in range(P):
    data = list(map(int, input().split()))
    T = data[0]
    heights = data[1:]
    
    line = []
    total_steps = 0
    
    for height in heights:
        pos = len(line)
        
        for i in range(len(line)):
            if line[i] > height:
                pos = i
                break
        
        total_steps += len(line) - pos
        line.insert(pos, height)
    
    print(T, total_steps)