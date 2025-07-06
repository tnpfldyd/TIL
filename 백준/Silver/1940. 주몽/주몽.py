import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
materials = list(map(int, input().split()))

materials.sort()

left = 0
right = n - 1
count = 0

while left < right:
    current_sum = materials[left] + materials[right]
    
    if current_sum == m:
        count += 1
        left += 1
        right -= 1
    elif current_sum < m:
        left += 1
    else:
        right -= 1

print(count)