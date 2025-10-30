import sys
input = sys.stdin.readline

n, m = map(int, input().split())

courses = []
for _ in range(n):
    P, L = map(int, input().split())
    mileages = list(map(int, input().split()))
    
    mileages.sort(reverse=True)
    
    if P < L:
        required = 1
    else:
        required = mileages[L - 1]
    
    courses.append(required)

courses.sort()

count = 0
total = 0
for required in courses:
    if total + required <= m:
        total += required
        count += 1

print(count)