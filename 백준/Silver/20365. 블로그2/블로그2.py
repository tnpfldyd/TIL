import sys
input = sys.stdin.readline

N = int(input())
colors = input().strip()

def solve(start_color):
    operations = 1
    i = 0
    while i < N:
        if colors[i] != start_color:
            operations += 1
            current_color = colors[i]
            while i < N and colors[i] == current_color:
                i += 1
        else:
            i += 1
    return operations

print(min(solve('R'), solve('B')))