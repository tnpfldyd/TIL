import sys
input = sys.stdin.readline

def solve_case():
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, category = input().split()
        if category not in clothes:
            clothes[category] = []
        clothes[category].append(name)
    
    result = 1
    for category in clothes:
        result *= (len(clothes[category]) + 1)
    
    return result - 1

t = int(input())
for _ in range(t):
    print(solve_case())