import sys
input = sys.stdin.readline
N, M = map(int, input().split())
total = int(input())
mis = int(input())

arr = []
max_x = 0

for i in range(mis):
    x, y = map(int, input().split())
    max_x = max(max_x, x)
    arr.append(y)

arr.sort()

left, right = max_x, 1000000

def check(w):
    prev = arr[0]
    ret = 1
    for i in range(1, mis):
        if prev + w <= arr[i]:
            prev = arr[i]
            ret += 1
    
    return ret

result = left

while left < right:
    mid = (left + right) // 2
    temp = check(mid)
    if temp > total:
        left = mid + 1
        result = left

    else:
        right = mid

print(result)