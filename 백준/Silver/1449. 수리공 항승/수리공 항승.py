import sys
input = sys.stdin.readline

n, l = map(int, input().split())
positions = list(map(int, input().split()))
positions.sort()

tape_count = 0
i = 0

while i < n:
    start = positions[i] - 0.5
    tape_end = start + l
    
    while i < n and positions[i] + 0.5 <= tape_end:
        i += 1
    
    tape_count += 1

print(tape_count)