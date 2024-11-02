import sys

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))
sorted_arr = arr[:]
index_map = {value: idx for idx, value in enumerate(arr)}

sorted_arr.sort()

ans = 0
for i in range(n):
    if sorted_arr[i] == arr[i]:
        continue
    j = index_map[sorted_arr[i]]
    index_map[sorted_arr[i]] = i
    index_map[arr[i]] = j
    arr[i], arr[j] = arr[j], arr[i]
    ans += 1

print(ans)