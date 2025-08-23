import sys
input = sys.stdin.readline

N = int(input())
ingredients = []
for _ in range(N):
    s, b = map(int, input().split())
    ingredients.append((s, b))

min_diff = float('inf')

for mask in range(1, 1 << N):
    sour = 1
    bitter = 0
    
    for i in range(N):
        if mask & (1 << i):
            sour *= ingredients[i][0]
            bitter += ingredients[i][1]
    
    min_diff = min(min_diff, abs(sour - bitter))

print(min_diff)