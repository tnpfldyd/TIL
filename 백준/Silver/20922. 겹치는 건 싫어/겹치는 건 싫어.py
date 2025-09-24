import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

count = {}
left = 0
max_length = 0

for right in range(N):
    count[arr[right]] = count.get(arr[right], 0) + 1
    
    while count[arr[right]] > K:
        count[arr[left]] -= 1
        if count[arr[left]] == 0:
            del count[arr[left]]
        left += 1
    
    max_length = max(max_length, right - left + 1)

print(max_length)